# GulfGate 海湾之门 · 出海判断力训练助手

<p><a href="README.md"><u>简体中文</u></a> · <a href="README.en.md"><u>English</u></a> · <a href="README.ar.md"><u>العربية</u></a></p>

<div align="center">
  <img src="docs/images/hero-training.png" alt="GulfGate Country Training Skill hero" width="100%">
</div>

> 让出海新人先在安全情境里做判断、看后果，再带着可追溯的行为证据上岗。

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-compatible-1f6f50)](SKILL.md)
[![Scenarios](https://img.shields.io/badge/scenarios-38-c18b49)](#训练路线)
[![Arabic](https://img.shields.io/badge/Arabic%20audio-379%20terms-1f6f50)](#阿语随身听)
[![Validation](https://img.shields.io/badge/tests-passing-2f7d55)](tests/validate_package.py)

学员进入可解释的海湾业务情境，做一次主要判断；系统先展示业务后果，再发知识卡，并依据真实行为形成能力证据。每一次训练都会留下可用于复盘和岗位培养的具体依据。

它适合：

- 出海销售、项目、法务、合规和交付岗位的新员工培训；
- 校招或社招面试中的情境化能力观察；
- 希望把产品知识转化为客户、伙伴与风险判断力的销售团队；
- 企业内训中的统一业务语言、风险底线和升级路径教学。

## 一套训练，直接得到四类结果

- **即时反馈**：选择之后马上看到业务后果、关键判断和更优动作；
- **能力证据**：按 A1–A6 沉淀表现，区分已展示、发展中与待观察能力；
- **定制路线**：按岗位、国家、行业和训练时长自动组合情境；
- **培训报告**：输出个人复盘、优势标签、待加强主题和下阶段训练建议。

## 三个高频训练案例

<div align="center">
  <img src="docs/images/cases-training.png" alt="Three Gulf business training use cases" width="100%">
</div>

1. **新能源销售新人 · 20 分钟快速版**：从客户拜访、伙伴核查到准入与回款，快速建立业务判断框架。
2. **法务 / 合规岗位 · 职责版**：围绕许可、合同、数据、制裁和危机升级，训练证据意识与专业边界。
3. **HR / 团队培养 · 全景版**：完成模块画像、团队共性与训练重点，生成授权范围内的培养报告。

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

能力评估聚焦 E2 有效证据与 E3 强证据，按 OBSERVE、REASON、DECIDE、ACT、VERIFY、ESCALATE、REVISE 七个取证维度记录学员自己的判断、理由和行动，让反馈贴近真实工作表现。

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

包内提供基于 Python 3 标准库的检索工具，`references/knowledge/` 中的 TXT/CSV 也可以直接读取。

## 阿语随身听

训练包包含 379 条阿语索引和 369 个 MP3 文件，覆盖问候、餐饮、商务、合规、行业等高频主题。剧情出现已收录词时，可以自动生成本轮词汇点读链接，让学员边看业务语境边听发音。

播放器支持本轮词汇聚合、完整词库筛选和逐词播放，并与训练进度、笔记和画像保持独立。

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

每一次内容更新都会自动复验知识索引、音频路径、哈希值和检索脚本，持续保障训练材料与发布版本的一致性。

## 隐私与报告

- 个人笔记默认私密，并按用户授权范围处理；
- HR 与团队报告支持明确授权和范围控制；
- 保存进度前会确认写入成功，保障复盘记录可靠；
- 纯聊天环境会在当前上下文中维护进度；
- 私人笔记、答案和画像与可分发 Skill 文件保持分离。

## 实时核验能力

训练涉及真实报价、投标、发货、清关、派驻、税务、医疗、产品安全、数据跨境和制裁时，会进入 LIVE_VERIFY 流程，以主管机关和官方正文作为事实依据。

宿主具备网页搜索和正文读取能力时，可以完成当次实时核验；包内知识库则持续支持训练背景、业务推演和补证清单。

## 同系列项目

真实业务研究、市场进入和行动前预检使用独立的 [GulfGate 国别研判助手](https://github.com/origami3521905038-hash/gulfgate-country-analysis)。

## 共创者

本项目由 [@origami3521905038-hash](https://github.com/origami3521905038-hash)、[@18719203981lkr-spec](https://github.com/18719203981lkr-spec)、[@konczgrignani409-blip](https://github.com/konczgrignani409-blip)、[@yao132517-byte](https://github.com/yao132517-byte) 和 [@m17783458051-tutu](https://github.com/m17783458051-tutu) 共同完成。

完整贡献记录见 [CONTRIBUTORS.md](CONTRIBUTORS.md)。欢迎提交岗位情境、来源核验、能力证据规则、阿语听审与跨宿主测试。协作规范见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可

版权归五位共创者共同所有。欢迎就企业培训、课程定制、行业扩展和合作授权联系作者。

