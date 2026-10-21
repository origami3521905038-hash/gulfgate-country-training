# 知识目录与调用路由

知识文件保留适用边界、日期和证据状态；读取记录正文时同时读取文件头。精确编号检索是入口，不取代范围判断。

## 载入时机

每次启用必读：KB_00（运行规则与知识索引）。其余按需定位，不整包注入：主线/路线读 KB_01＋KB_06；情境出题读当前 Pxx＋KB_06 映射＋对应国别行业记录；反馈读对应 KB_Q；官方事实核验读 KB_02；复盘/报告读 KB_03；专题补证读 KB_topic_M1–M7（仅主要材料不足时）；国别/行业适配读 KB_04/KB_05 与对应文件。

| 模式 | 读取材料 |
|---|---|
| INTAKE | 完整运行规则第五节；不常规搜索知识 |
| ROUTE | KB_01＋KB_06，quick七节点；role 18–28；panorama 38 |
| SCENARIO出题 | 当前Pxx、KB_06映射、所需国家与行业记录；不提前显示反馈答案 |
| SCENARIO反馈 | 已展示题目及证据＋相应KB_Q；其他情境定向组成完整4–6卡 |
| BRANCH/FREE_QA | 当前问题对应记录；支线保留return_to_scenario_id |
| ANALYSIS_BRANCH | 原情境、待判断问题和return_to_scenario_id；把必要国别、产品、角色、交易模式与约束交给同级研判 Skill，不整包注入训练知识 |
| REVIEW/REPORT | KB_03＋授权证据与必要原话；不遍历全知识库 |
| LIVE_VERIFY | KB_02对应条目→宿主官方网页检索与正文核验 |
| 国别/行业适配 | 必要时KB_04/KB_05，国家和行业文件按适用维度分别叠加 |
| 专题补证 | KB_topic_M1–M7，仅主要材料不足时定向读取 |
| 术语 | terms.csv或terms.jsonl，按名称/近义词定位；保留原释义和四段式阿语 |

## 全部知识文件

- [KB_00_运行规则与知识索引](knowledge/KB_00_运行规则与知识索引.txt)
- [KB_01_七模块与38情境](knowledge/KB_01_七模块与38情境.txt)
- [KB_02_官方来源白名单](knowledge/KB_02_官方来源白名单.txt)
- [KB_03_能力证据与报告规则](knowledge/KB_03_能力证据与报告规则.txt)
- [KB_04_国别基本盘速查](knowledge/KB_04_国别基本盘速查.txt)
- [KB_05_三层行业属性与术语包索引](knowledge/KB_05_三层行业属性与术语包索引.txt)
- [KB_06_情境取材与quick前置背景](knowledge/KB_06_情境取材与quick前置背景.txt)
- [KB_country_AE_阿联酋](knowledge/KB_country_AE_阿联酋.txt)
- [KB_country_BH_巴林](knowledge/KB_country_BH_巴林.txt)
- [KB_country_KW_科威特](knowledge/KB_country_KW_科威特.txt)
- [KB_country_OM_阿曼](knowledge/KB_country_OM_阿曼.txt)
- [KB_country_QA_卡塔尔](knowledge/KB_country_QA_卡塔尔.txt)
- [KB_country_SA_沙特](knowledge/KB_country_SA_沙特.txt)
- [KB_industry_I1_新能源](knowledge/KB_industry_I1_新能源.txt)
- [KB_industry_I2_建材与工程承包](knowledge/KB_industry_I2_建材与工程承包.txt)
- [KB_industry_I3_跨境电商与消费电子](knowledge/KB_industry_I3_跨境电商与消费电子.txt)
- [KB_industry_I4_医疗器械](knowledge/KB_industry_I4_医疗器械.txt)
- [KB_industry_I5_轻工业产品](knowledge/KB_industry_I5_轻工业产品.txt)
- [KB_Q_P04_市场进入假设](knowledge/KB_Q_P04_市场进入假设.txt)
- [KB_Q_P07_伙伴能力与职责](knowledge/KB_Q_P07_伙伴能力与职责.txt)
- [KB_Q_P13_热情与真实承诺](knowledge/KB_Q_P13_热情与真实承诺.txt)
- [KB_Q_P17_准入与规则有效性](knowledge/KB_Q_P17_准入与规则有效性.txt)
- [KB_Q_P23_付款节点与保障](knowledge/KB_Q_P23_付款节点与保障.txt)
- [KB_Q_P28_批次质量与交付](knowledge/KB_Q_P28_批次质量与交付.txt)
- [KB_Q_P35_行业事件与责任](knowledge/KB_Q_P35_行业事件与责任.txt)
- [KB_Q_P38_综合复盘与新证据](knowledge/KB_Q_P38_综合复盘与新证据.txt)
- [KB_topic_M1_国别与市场机会](knowledge/KB_topic_M1_国别与市场机会.txt)
- [KB_topic_M2_商业生态与进入路径](knowledge/KB_topic_M2_商业生态与进入路径.txt)
- [KB_topic_M3_跨文化接触与关系推进](knowledge/KB_topic_M3_跨文化接触与关系推进.txt)
- [KB_topic_M4_产品、项目准入与投标](knowledge/KB_topic_M4_产品、项目准入与投标.txt)
- [KB_topic_M5_合同、金融与回款](knowledge/KB_topic_M5_合同、金融与回款.txt)
- [KB_topic_M6_交付、本地运营与增长](knowledge/KB_topic_M6_交付、本地运营与增长.txt)
- [KB_topic_M7_合规、危机与持续经营](knowledge/KB_topic_M7_合规、危机与持续经营.txt)

## 本地检索示例

在技能目录中，用当前平台可用的 Python 3 执行（无 Python 则直接读取原文件）：

```text
python scripts/lookup.py record P17
python scripts/lookup.py record AE_TDRA_TA
python scripts/lookup.py record C-AE-M4-01
python scripts/lookup.py search 无线 --file KB_industry_I3 --limit 3
python scripts/lookup.py term gahwa
```

record 返回同编号的所有命中，不假定跨文件编号唯一。search 为文字检索，--file 按原文件名前缀限制范围；不是语义检索，未命中不证明知识不存在。每次输出命中总数及是否截断，默认不注入全库。若需完整文件，按本目录链接读取。
