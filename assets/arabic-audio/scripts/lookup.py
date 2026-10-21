#!/usr/bin/env python3
"""GulfGate（海湾之门） 阿语发音查询（纯离线，精确匹配 + 近似匹配）。

用法：
    python3 scripts/lookup.py "isalam aleikum"        # 单条查询，输出 JSON
    python3 scripts/lookup.py "咖啡" --search 5       # 返回前 5 个候选
    python3 scripts/lookup.py --stats                 # 词表概览
    python3 scripts/lookup.py --check                 # 校验音频文件完整性
    python3 scripts/lookup.py --batch queries.txt     # 批量查询（每行一条）

给智能体的约定：
    status=ok        → 在阿语后面附 page_url（“▶ 听发音”），不要改写音频路径
    status=not_found → 只显示文字；可参考 suggestions 里的近似词
    status=ambiguous → 存在多个可能，先用中文向用户确认，不要猜
本脚本不联网、不生成新音频、不修改任何文件。
"""
import argparse
import difflib
import json
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parent

FUZZY_CUTOFF = 0.84      # 近似匹配阈值
FUZZY_MARGIN = 0.04      # 最佳候选与次优候选的最小差距，避免误配


def norm(text: str) -> str:
    """归一化：去掉阿语变音符号/标点、拉丁重音、大小写与所有空白和符号。"""
    if text is None:
        return ""
    text = unicodedata.normalize("NFKD", str(text))
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u0640]", "", text)
    text = re.sub(r"[\u060C\u061B\u061F.,!?'’\"`\-_/\\()\[\]]", "", text)
    text = re.sub(r"\s+", "", text)
    return text.casefold()


def load(pkg: Path):
    payload = json.loads((pkg / "terms.json").read_text(encoding="utf-8"))
    terms = payload["terms"] if isinstance(payload, dict) else payload
    for t in terms:                       # 预算好归一化字段，匹配时直接复用
        t["_aliases"] = {norm(a) for a in t.get("aliases", []) if a and norm(a)}
        t["_aliases"].add(norm(t["term"]))
        t["_meaning"] = norm(t["meaning"])
        t["_term"] = norm(t["term"])
    return payload, terms, None


def describe(t: dict, pkg: Path) -> dict:
    page = pkg / "player.html"
    audio = pkg / t["audio"]
    page_url = page.as_uri() + "#" + t["id"]
    return {
        "status": "ok",
        "id": t["id"],
        "index": t.get("index"),
        "category": t.get("category"),
        "term": t["term"],
        "arabic": t["arabic"],
        "transliteration": t["transliteration"],
        "chinese_sound": t["chinese_sound"],
        "meaning": t["meaning"],
        "synonyms": t.get("synonyms", []),
        "note": t.get("note", ""),
        "duration": t.get("duration"),
        "review": t.get("review"),
        "page_url": page_url,
        "page_path": str(page),
        "page_ref": f"player.html#{t['id']}",
        "audio_path": str(audio),
        "audio_url": audio.as_uri(),
        "audio_exists": audio.is_file(),
    }


def _dedupe_by_audio(cands: list) -> list:
    """同一段音频（同一个词）只保留序号最小的一条，其余作为别名附注。"""
    groups = {}
    for t in sorted(cands, key=lambda x: x["index"]):
        groups.setdefault(t["audio"], []).append(t)
    out = []
    for _, members in groups.items():
        head = dict(members[0])
        others = [m["term"] for m in members[1:]]
        if others:
            head["also_listed_as"] = others
        out.append(head)
    return sorted(out, key=lambda x: x["index"])


def lookup(query: str, terms: list, index=None, pkg: Path = None, top: int = 1) -> dict:
    q = norm(query)
    if not q:
        return {"status": "empty", "query": query}

    tiers = [
        ("term_exact", [t for t in terms if t["_term"] == q]),
        ("alias_exact", [t for t in terms if q in t["_aliases"]]),
        ("alias_partial", [t for t in terms if any(q in a for a in t["_aliases"])]),
        ("meaning_partial", [t for t in terms if q in t["_meaning"]]),
    ]
    matched = None
    for name, cands in tiers:
        if cands:
            # 同一层级里若只有一条是“人工补充别名”命中（相对于 CSV 近义词），优先采用它。
            if name in ("alias_exact", "alias_partial") and len({c["audio"] for c in cands}) > 1:
                curated = [c for c in cands
                           if any(norm(x) == q for x in c.get("extra_aliases", []))]
                if len({c["audio"] for c in curated}) == 1 and curated:
                    cands = curated
            matched = (name, _dedupe_by_audio(cands))
            break

    if not matched:
        scored = []
        for t in terms:
            best = max((difflib.SequenceMatcher(None, q, a).ratio() for a in t["_aliases"]), default=0)
            if best >= FUZZY_CUTOFF:
                scored.append((best, t))
        scored.sort(key=lambda x: -x[0])
        if scored and (len(scored) == 1 or scored[0][0] - scored[1][0] >= FUZZY_MARGIN):
            matched = ("fuzzy", _dedupe_by_audio([t for _, t in scored[:3]]))
        else:
            near = [{"term": t["term"], "id": t["id"], "arabic": t["arabic"]}
                    for _, t in sorted(scored, key=lambda x: -x[0])[:3]]
            return {"status": "not_found", "query": query, "suggestions": near}

    tier, cands = matched
    if top > 1:
        return {"status": "ok", "query": query, "match": tier, "count": len(cands),
                "results": [describe(t, pkg) for t in cands[:top]]}
    if len(cands) > 1:
        return {
            "status": "ambiguous",
            "query": query,
            "match": tier,
            "candidates": [{k: t[k] for k in ("id", "term", "arabic", "chinese_sound", "meaning")} for t in cands],
            "hint": "同一写法对应多个词条，请先确认要哪一个，再按 id 查询；不确定时用中文向用户确认。",
        }
    res = describe(cands[0], pkg)
    res["match"] = tier
    if cands[0].get("also_listed_as"):
        res["also_listed_as"] = cands[0]["also_listed_as"]
    return res


def by_id(terms: list, tid: str):
    for t in terms:
        if t["id"] == tid:
            return t
    return None


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="GulfGate（海湾之门） 阿语发音查询（离线）")
    ap.add_argument("query", nargs="?", help="阿语原文 / 拉丁转写 / 中文音译 / 中文释义 / 术语名")
    ap.add_argument("--pkg", default=str(PKG), help="音频包目录（默认脚本所在包）")
    ap.add_argument("--search", type=int, default=0, help="返回前 N 个候选")
    ap.add_argument("--stats", action="store_true", help="输出词表概览")
    ap.add_argument("--check", action="store_true", help="校验音频文件是否齐全")
    ap.add_argument("--batch", help="批量查询文件（每行一条）")
    ap.add_argument("--pretty", action="store_true", help="缩进输出")
    args = ap.parse_args()

    pkg = Path(args.pkg).resolve()
    payload, terms, index = load(pkg)
    meta = payload.get("_meta", {}) if isinstance(payload, dict) else {}

    if args.stats:
        cats = {}
        for t in terms:
            cats[t["category"]] = cats.get(t["category"], 0) + 1
        print(json.dumps({
            "package": str(pkg),
            "term_count": len(terms),
            "audio_count": len({t["audio"] for t in terms}),
            "categories": cats,
            "meta": meta,
        }, ensure_ascii=False, indent=2))
        return 0

    if args.check:
        missing = [t["id"] for t in terms if not (pkg / t["audio"]).is_file()]
        silent = [t["id"] for t in terms if (t.get("mean_volume_db") or 0) < -50 and t.get("mean_volume_db") is not None]
        no_review = [t["id"] for t in terms if t.get("review") != "用户听审通过"]
        print(json.dumps({
            "term_count": len(terms),
            "missing_audio": missing,
            "suspected_silence": silent,
            "pending_review_count": len(no_review),
            "ok": not missing and not silent,
        }, ensure_ascii=False, indent=2))
        return 0 if not missing and not silent else 1

    if args.batch:
        lines = [l.strip() for l in Path(args.batch).read_text(encoding="utf-8").splitlines() if l.strip()]
        for line in lines:
            res = lookup(line, terms, index, pkg, args.search or 1)
            print(json.dumps(res, ensure_ascii=False))
        return 0

    if not args.query:
        ap.error("需要查询词，或使用 --stats / --check / --batch")
    res = lookup(args.query, terms, index, pkg, args.search or 1)
    print(json.dumps(res, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0 if res.get("status") == "ok" else 1


if __name__ == "__main__":
    sys.exit(main())
