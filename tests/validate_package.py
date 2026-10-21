#!/usr/bin/env python3
"""Offline release checks for the GulfGate country-training skill."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


def check_frontmatter() -> str:
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise AssertionError("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise AssertionError("SKILL.md frontmatter is not closed")
    frontmatter = text[4:end]
    name = re.search(r"^name:\s*(\S+)\s*$", frontmatter, re.MULTILINE)
    description = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
    if not name or name.group(1) != "gulfgate-country-training":
        raise AssertionError("unexpected skill name")
    if not description or len(description.group(1).strip()) < 80:
        raise AssertionError("description is missing or too short")
    return name.group(1)


def check_links() -> int:
    checked = 0
    missing: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".txt", ".html"}:
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            checked += 1
            if not (path.parent / target).resolve().exists():
                missing.append(f"{path.relative_to(ROOT)} -> {target}")
    if missing:
        raise AssertionError("broken local links:\n" + "\n".join(missing))
    return checked


def check_audio() -> tuple[int, int]:
    audio_root = ROOT / "assets/arabic-audio"
    terms = json.loads((audio_root / "terms.json").read_text(encoding="utf-8"))["terms"]
    ids = [item["id"] for item in terms]
    if len(ids) != len(set(ids)):
        raise AssertionError("duplicate Arabic term IDs")
    missing: list[str] = []
    hash_mismatches: list[str] = []
    for item in terms:
        audio = audio_root / item["audio"]
        if not item.get("has_audio") or not audio.is_file():
            missing.append(item["id"])
            continue
        digest = hashlib.sha256(audio.read_bytes()).hexdigest()
        if item.get("sha256") and digest != item["sha256"]:
            hash_mismatches.append(item["id"])
    if missing:
        raise AssertionError("audio paths missing: " + ", ".join(missing))
    if hash_mismatches:
        raise AssertionError("audio hashes do not match: " + ", ".join(hash_mismatches))
    files = list((audio_root / "assets/audio").glob("*.mp3"))
    if len(files) < 300:
        raise AssertionError("audio set is unexpectedly small")
    return len(terms), len(files)


def check_record_index() -> tuple[int, int]:
    index = json.loads((ROOT / "references/record-index.json").read_text(encoding="utf-8"))
    cache: dict[Path, list[str]] = {}
    for item in index:
        path = (ROOT / item["file"]).resolve()
        if ROOT not in path.parents or not path.is_file():
            raise AssertionError(f"invalid record index path: {item['file']}")
        lines = cache.setdefault(path, path.read_text(encoding="utf-8-sig").splitlines())
        if item["start_line"] < 1 or item["end_line"] < item["start_line"] or item["end_line"] > len(lines):
            raise AssertionError(f"invalid record line range: {item['id']}")
    knowledge_files = list((ROOT / "references/knowledge").glob("*.txt"))
    if len(knowledge_files) < 30:
        raise AssertionError("knowledge file set is unexpectedly small")
    return len(index), len(knowledge_files)


def check_lookup() -> int:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts/lookup.py"), "term", "gahwa", "--limit", "1"],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    if payload.get("matches", 0) < 1:
        raise AssertionError("term lookup smoke test failed")
    return payload["returned"]


def main() -> None:
    name = check_frontmatter()
    links = check_links()
    terms, audio_files = check_audio()
    records, knowledge_files = check_record_index()
    returned = check_lookup()
    print(
        json.dumps(
            {
                "status": "passed",
                "skill": name,
                "local_links": links,
                "knowledge_files": knowledge_files,
                "indexed_records": records,
                "audio_terms": terms,
                "audio_files": audio_files,
                "lookup_results": returned,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

