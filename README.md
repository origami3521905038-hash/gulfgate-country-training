# GulfGate 海湾之门 · 出海判断力训练助手

[简体中文](README.md) · [English](README.en.md) · [العربية](README.ar.md)

<div align="center">
  <img src="docs/images/hero-training.png" alt="GulfGate Country Training Skill hero" width="100%">
</div>

> 让出海新人先在安全情境里做判断、看后果，再带着可追溯的行为证据上岗。

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-compatible-1f6f50)](SKILL.md)
[![Scenarios](https://img.shields.io/badge/scenarios-38-c18b49)](#训练路线)
[![Arabic](https://img.shields.io/badge/Arabic%20audio-379%20terms-1f6f50)](#阿语随身听)
[![Validation](https://img.shields.io/badge/tests-passing-2f7d55)](tests/validate_package.py)

这不是刷题工具，也不是“点击正确答案拿积分”的考试。学员进入可解释的海湾业务情境，做一次主要判断；系统先演后果，再发知识卡，并只根据真实行为记录能力证据。

它适合：

- 出海销售、项目、法务、合规和交付岗位的新员工培训；
- 校招或社招面试中的情境化能力观察；
- “会说产品，但不会判断客户、伙伴和风险”的销售训练；
- 企业内训中的统一业务语言、风险底线和升级路径教学。

## 真实使用示例

<div align="center">
  <img src="docs/images/demo-training.png" alt="Country training demo session" width="100%">
</div>

示例输入：

```text
使用 $gulfgate-country-training。
我是新能源出海销售新人，重点看沙特和阿联酋。
想练伙伴判断、产品准入和回款风险，走约 20 分钟的快速路线。
```

完整匿名交互见 [examples/training-demo.md](examples/training-demo.md)。

## 它会训练什么

| 能力 | 训练重点 |
| --- | --- |
| A1 国别判断 | 区分国家、酋长国、自由区、项目法域和事实时效 |
| A2 跨文化沟通 | 识别关系、场景、称呼、会面和推进信号 |
| A3 准入判断 | 分开产品、企业、项目、平台和供应商资格 |
| A4 合规意识 | 识别许可、反腐、税务、数据和人员边界 |
| A5 风险治理 | 设计证据、阶段闸门、升级与退出条件 |
| A6 交付执行 | 从报价、合同、物流、安装、验收到回款形成闭环 |

能力评估使用 E0–E3：

- E0 未观察：旁听、索取答案或无关回答；
- E1 弱证据：方向合理，但缺少理由或行动；
- E2 有效证据：判断、理由和行动基本完整；
- E3 强证据：能处理冲突、核验边界，并在新证据下修正。

题内给出的理由不能冒充学员自己的独立推理。

## 训练路线

| 路线 | 情境数 | 适合场景 |
| --- | ---: | --- |
| `quick` 快速版 | 7 | 约 20 分钟的岗位入门或团队热身 |
| `role` 职责版 | 18–28 | 按销售、法务、项目、合规等职责组合定制 |
| `panorama` 全景版 | 38 | 走完整业务链，适合系统培训和综合复盘 |

七个模块覆盖：国别与市场机会、商业生态与进入路径、跨文化接触与关系推进、产品与项目准入、合同金融与回款、交付与本地运营、合规危机与持续经营。

## 安装

```bash
git clone https://github.com/origami3521905038-hash/gulfgate-country-training.git
mkdir -p ~/.codex/skills
cp -R gulfgate-country-training ~/.codex/skills/
```

必须复制整个目录。训练规则、33 个知识文件、检索索引、术语和音频都在包内。

运行离线校验：

```bash
cd gulfgate-country-training
python tests/validate_package.py
```

脚本只使用 Python 3 标准库。没有 Python 时，仍然可以直接读取 `references/knowledge/` 中的 TXT/CSV。

## 阿语随身听

训练包包含 379 条阿语索引和 369 个 MP3 文件，按问候、餐饮、商务、合规、行业等主题组织。剧情出现已收录词时，可以生成本轮词汇点读链接。

注意：

- 音频由 macOS Majed 机器合成，不是真人录音；
- 379 条仍标记为“未逐条人工听审”；
- 不宣称零发音错误；
- 播放器不会同步或接收训练答案、笔记和画像。

## 测试证据

<div align="center">
  <img src="docs/images/test-training.png" alt="Country training validation results" width="100%">
</div>

发布检查覆盖：

- `SKILL.md` frontmatter 与本地资源链接；
- 33 个知识文件与 1,931 条记录索引；
- 379 个词条 ID 的音频路径与 SHA-256；
- 369 个实际 MP3 文件；
- 本地术语检索；
- GitHub Actions 自动校验。

测试证明包和音频资产可读、索引一致、脚本可运行，不代表训练效果已经完成大规模统计验证。

## 隐私与报告

- 个人笔记默认私密；
- HR 或团队报告必须获得明确授权；
- 没有成功写入存储时，不能声称已经保存；
- 纯聊天环境应只在当前可见上下文内维护进度；
- 私人笔记、答案和画像不得回写 Skill 文件或知识库。

## 事实边界

训练材料中的政策和规则只是练习背景。涉及真实报价、投标、发货、清关、派驻、税务、医疗、产品安全、数据跨境和制裁时，必须触发 LIVE_VERIFY，以当次官方正文为准。

本 Skill 不附带搜索账号、API Key 或后台任务。宿主没有联网权限时，应明确保留待核验项。

## 同系列项目

真实业务研究、市场进入和行动前预检使用独立的 [GulfGate 国别研判助手](https://github.com/origami3521905038-hash/gulfgate-country-analysis)。

## 共创者

本项目由 [@origami3521905038-hash](https://github.com/origami3521905038-hash) 与 [@18719203981lkr-spec](https://github.com/18719203981lkr-spec) 共同完成。

欢迎提交岗位情境、来源核验、能力证据规则、阿语听审与跨宿主测试。协作规范见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可

本仓库暂未附加开放许可证。版权归共创者所有；公开复用、商业使用或再分发前，请先取得作者书面许可。

