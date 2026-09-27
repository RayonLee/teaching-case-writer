# teaching-case-writer

**中文** | [English](#english)

中文商学院教学案例写作 skill：素材审计 → 事实核查 → 决策主线叙事 → 案例↔笔记协作成对 → 统一排版 → 三层核验，按人大／管理案例共享中心投稿格式交付案例正文与教学笔记。
A Coding Agent skill for writing Chinese business-school teaching cases: material audit → fact-checking → decision-spine narrative → paired case & teaching note → uniform typesetting → three-layer verification, delivered in RUC/CMCC submission format.

> **⚠️ PS（请务必阅读）：警惕使用 AI 工具进行学术与教学内容创作。** 本 skill 仅为案例写作流程的辅助工具与经验沉淀。AI 生成内容可能存在事实错误与口径偏差；案例涉及的真实企业、人物与数据必须由作者本人逐条核验，涉真实主体的案例投稿前请自行确认授权与合规，作者对最终文本承担全部责任。

---

## 中文

一套教学案例写作工作流：先对素材或旧稿做**结构审计**（主角是否决策人、有无决策场景、数据是否有出处、结尾是否泄露结论、案例与笔记是否断链），联网核查事实并建立来源档案，以**决策主线**重写案例正文（决策场景开场、十进制小节、开放结尾、文末字数标记），再以**协作结构**撰写配套教学笔记（九节固定结构、5 道递进思考题、四段式参考答案、映射表、分钟级板书计划），最后用脚本排版为审定格式 docx 并执行三层核验后交付。

### 实战成果

本 Skill 沉淀自真实案例精修项目：对 **4 对 8 篇**教学案例（将门创投、老饭骨、AI 编程成本豪赌、上清北）完成「审计 → 重写 → 人大格式返修 → 统一 → 核验」全流程。交付指标：案例正文 9,605–9,869 字（区间 8,000–10,000）、教学笔记 11,060–13,472 字（区间 10,000–14,000）、1,630+ 处直引号全量转中文引号、3 类批量转换损伤（标题降级／小标题污染／散文漏枚举）全部在核验层被拦截修复，8 篇成品逐篇通过硬性约束机器断言。

### 设计思路

- **人定标准、AI 交付、人来验收**：案例格式以作者审定的一对参考稿为唯一标准，Agent 负责审计、调研、撰写、排版与自检，人只做立项确认与最终验收；验收满意的流程随即固化为 Skill。
- **经验在积累，而非流失**：SKILL.md 里每条规则都是真实踩坑的沉淀——批量转换后必须机器复检（三类转换损伤实录）、案例与笔记同批修改防断链、字数双口径（字符／Word）差异、主角不是决策人时的两种重构策略……全部写明原因与对策。
- **四套公开 skill 杂糅，只取所需**：取 case-study-writer 的决策主线与事实纪律、thws case-builder 的讨论计划设计、portfolio 的量化纪律、social-data-analysis 的文献不编造原则；弃其格式管线与领域专属框架。
- **案例与笔记是同一教学设计的两面**：讨论题从案例决策点生长，案例不泄露的结局只在笔记中交代，答案引用的数字与正文逐字一致。

### 核心优势

- **决策主线，而非编年史**：每篇案例只有一个决策主线——主角、压力、备选、证据、决策点；开场 300 字内出现主角与待决问题，结尾停在开放抉择，把判断留给课堂。
- **案例↔笔记协作结构**：5 道思考题按「诊断→分析→评价→决策→延伸」递进，逐题对应案例情节锚点；「案例问题 × 理论知识点 × 案例情节」映射表让题—理论—情节的对齐一目了然。
- **排版脚本复刻审定格式**：幼圆 16pt 标题页、宋体小四 1.5 倍行距、对话自动楷体、真实 Word 标题样式（导航可用）、图 N 加粗图注、文末自动生成「（案例正文完，全文X字）」标记。
- **三层核验闭环**：机器核验（重开 docx 逐项断言字数、结构、引号、元文本）＋人工研判（开场、结尾、答案四段式）＋协作核验（题目锚点、数字一致、结局隔离），全部通过才允许交付。

### 硬性约束（也是亮点）

- **案例正文**：8,000–10,000 字；摘要 200–300 字＋关键词；决策场景开场；开放结尾不泄结局；无讨论题、无适用课程（均属笔记）；数据有出处或标注演绎；全中文引号；文末字数标记。
- **教学笔记**：10,000–14,000 字；九节固定顺序（摘要／教学目标／教学对象／启发思考题／板书计划／思考题分析／背景信息／关键要点／参考文献）；思考题恰好 5 道；每题答案 =【理论依据】+ 理论展开 + 案例结合 +【案例分析】；含映射表与分钟级板书计划。
- **事实纪律**：不编造事实、数字、引语、文献；真实主体附资料来源与免责声明，化名案例卷首声明全部数据为教学演绎；查不到的精确数字改定性表述，绝不「圆梦」。

### 日常使用：一句话 Prompt

在 Coding Agent（Kimi Code / Claude Code 等）中打开本文件夹，输入：

> 按 teaching-case-writer 的流程，把这份素材写成一对人大格式的教学案例与教学笔记，素材在 XXX.docx（或：把 XXX.docx 这篇旧案例按该流程拔高）

Agent 会先向你确认立项信息（案例主角／核心决策／目标受众／真实或化名／篇幅），随后按 [SKILL.md](SKILL.md) 执行完整流水线：素材审计 → 联网核查 → 案例撰写 → 笔记撰写 → 脚本排版 → 三层核验 → 交付。无需记忆任何命令。

也可将本文件夹放入你的 Agent skills 目录，「写教学案例 / 案例润色 / 教学笔记 / 案例投稿」类请求即可自动触发本 Skill。

### 交付物

| 层级 | 交付物 | 说明 |
|---|---|---|
| **最终** | 案例正文 docx | 人大投稿格式：标题页＋摘要关键词＋决策主线叙事＋开放结尾＋文末字数标记 |
| **最终** | 教学笔记 docx | 九节结构、5 道递进思考题、四段式参考答案、映射表、板书计划 |
| **最终** | 核验报告 | 三层核验逐项结果（机器断言＋人工研判＋协作对照） |
| 中间 | 草稿 md | 排版脚本的输入稿，留档备查 |
| 沉淀 | SKILL.md 更新 | 每次项目的新教训写回 Skill，下次不再踩坑 |

### 随附脚本（scripts/）

| 脚本 | 用途 | 用法 |
|---|---|---|
| `build_docx.py` | 将 Markdown 式草稿排版为审定格式 docx（幼圆标题／宋体正文／楷体对话／表格图注／文末字数自动统计） | `python build_docx.py 草稿.md 输出.docx` |

### 快速开始

```bash
pip install python-docx
```

1. 准备素材（企业资料、访谈、旧案例草稿均可）
2. 在 Coding Agent 中打开本文件夹，用上面的一句话 Prompt 发起任务
3. 回答 Agent 的立项确认（主角／决策点／受众／真实或化名／篇幅）
4. 流水线跑完后，在 Word/WPS 中打开成品复查排版，并核对核验报告

### 目录结构

```
├── SKILL.md                     # 完整工作流文档（五阶段流程、硬性约束总表、失败模式红旗清单）
├── references/                  # 规范库
│   ├── case-format.md           # 案例正文结构与文档格式规范
│   ├── teaching-note-format.md  # 教学笔记九节结构与格式规范
│   ├── narrative-style.md       # 叙事方式与文风（决策主线、量化纪律、开放结尾）
│   ├── collaboration-structure.md # 案例↔笔记协作结构
│   └── quality-checklist.md     # 三层核验清单（含转换后专项复核）
├── scripts/
│   └── build_docx.py            # 审定格式排版脚本
└── README.md
```

> ⚠️ 再次提醒：警惕使用 AI 工具进行学术与教学内容创作。请遵守所在机构与出版方关于 AI 工具使用的规定；涉真实企业与人物的案例，事实、数据与合规由作者本人负全部责任。

---

## English

A complete workflow for writing Chinese business-school teaching cases: audit the source material or legacy draft first (Is the protagonist the decision-maker? Is there a decision scene? Are data points sourced? Does the ending leak conclusions? Are the case and the note cross-linked?), verify facts online and archive sources, rewrite the case body along a **decision spine** (decision-scene opening, decimal subsections, open ending, word-count marker), then write the paired teaching note with a **collaboration structure** (nine fixed sections, five progressive discussion questions, four-part reference answers, a question–theory–plot mapping table, and a minute-by-minute board plan), and finally typeset into docx with a script and deliver after three-layer verification.

### Proven in Real Projects

This skill was distilled from a real case-polishing project: **4 pairs / 8 documents** (TheJiangmen VC, LaoFanGu, an AI-programming cost gamble, and a county-school EdTech case) went through the full audit → rewrite → RUC-format revision → unification → verification pipeline. Delivery metrics: case bodies 9,605–9,869 characters (target 8,000–10,000), teaching notes 11,060–13,472 (target 10,000–14,000), 1,630+ straight quotes converted to Chinese quotes, and three classes of batch-conversion injuries (demoted titles, polluted sub-headings, missing enumerations) all intercepted and repaired at the verification layer.

### Design Philosophy

- **Human sets the standard, AI delivers, human accepts**: a user-approved reference pair is the single format authority; the agent audits, researches, writes, typesets, and self-checks; humans only confirm scoping and give final acceptance — and any workflow that passes is codified into a Skill.
- **Experience compounds instead of leaking**: every rule in SKILL.md is a lesson from a real pitfall — mandatory machine re-checks after batch conversion, editing case and note in the same batch to prevent broken cross-references, dual word-count metrics, and two rescue strategies when the protagonist is not the decision-maker.
- **Four public skills blended, only what is needed**: decision spine and fact discipline from case-study-writer, discussion-plan design from thws case-builder, quantification discipline from portfolio-case-study-generator, and no-fabricated-citations from social-data-analysis.
- **Case and note are two faces of one teaching design**: questions grow out of the case's decision points; the outcome hidden from students lives only in the note; every figure quoted in an answer matches the case text verbatim.

### Core Strengths

- **Decision spine, not chronicle**: one protagonist, one pressure, alternatives, evidence, decision point; the opening 300 characters present the decision-maker and the pending question; the ending stops at an open choice.
- **Case↔note collaboration**: five questions progressing diagnosis → analysis → evaluation → decision → extension, each anchored to case plots; a question × theory × plot mapping table makes alignment explicit.
- **Typesetting script replicating the approved format**: 16pt YouYuan title page, 12pt SimSun body with 1.5 line spacing, KaiTi for dialogue, real Word heading styles, bold figure captions, and an automatic end-of-case word-count marker.
- **Three-layer verification**: machine assertions on reopened docx + human judgment on openings/endings/answer structure + case↔note cross-checks — no delivery unless all pass.

### Hard Constraints (Also Highlights)

- **Case body**: 8,000–10,000 words; 200–300-character abstract + keywords; decision-scene opening; open ending; no discussion questions (they live in the note); sourced or declared-fictional data; Chinese quotes only; end word-count marker.
- **Teaching note**: 10,000–14,000 words; nine fixed sections; exactly five progressive questions; each answer = theory basis → theory elaboration → case application → case analysis; mapping table and minute-level board plan included.
- **Fact discipline**: no fabricated facts, figures, quotes, or citations; real-world cases carry source lists and disclaimers; fictionalized cases declare all data as illustrative up front; unverifiable figures are rephrased qualitatively.

### One-Sentence Prompt

> Follow the teaching-case-writer workflow to turn the material in XXX.docx into a paired case body and teaching note in RUC submission format.

### Deliverables

| Tier | Deliverable | Notes |
|---|---|---|
| Final | Case body docx | RUC format: title page, abstract + keywords, decision-spine narrative, open ending, word-count marker |
| Final | Teaching note docx | Nine sections, five progressive questions, four-part answers, mapping table, board plan |
| Final | Verification report | Results of the three-layer checks |
| Working | Draft markdown | Input to the typesetting script |
| Compounding | SKILL.md updates | New lessons written back into the skill |

### Quick Start

```bash
pip install python-docx
```

1. Prepare material (company documents, interviews, or a legacy case draft).
2. Open this folder in your Coding Agent and use the one-sentence prompt above.
3. Answer the scoping questions (protagonist / decision point / audience / real or fictionalized / length).
4. Review the output in Word/WPS and check the verification report.

> ⚠️ Reminder: be cautious when using AI tools for academic and teaching content creation. Follow your institution's and publisher's rules on AI use; for cases involving real companies and people, the author bears full responsibility for facts, figures, and compliance.
