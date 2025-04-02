# rc_planner_ai_integration.md

> 更新时间：2025-03-31
> 项目：Polaris
> 描述：探索 AI 如何结构性协助 Resource Consent（RC） 申请流程中 Planner 的任务，并为后续 PM 视角的系统介入奠定基础。

---

## 一、Planner 在 RC 流程中的核心职责分解

| 阶段 | Planner 任务 | 来源制度 / 依据 |
|------|---------------|----------------|
| 文件接收阶段 | 确认所有顾问提交文件完整 | Checklist、Submission Requirements |
| 文件审核阶段 | 审查是否符合 RMA 相关要求 | RMA 条款，Local Council Guidelines |
| 草拟 AEE Report | 撰写评估报告并整合背景与影响评估 | AEE 格式、往期范文 |
| 文件补正协调 | 发现问题反馈给顾问、收集修改版本 | 往返沟通、文件版本控制 |
| 最终提交 | 整合所有文档并递交至 Console 网站 | Council 提交流程与命名规范 |
| S92 回应 | 回应 further info request，分配任务给顾问 | S92 回应模板与历史文档 |

---

## 二、AI 可协作的切入点分析（Planner视角）

| 工作环节 | AI 切入点 | AI 能力类型 | 所需准备 |
|----------|------------|----------------|------------|
| Checklist 核查 | 自动比对文件清单缺漏 | 文档识别 + 模板匹配 | 提供标准化 checklist JSON |
| 顾问文档审核 | 判断文件内容是否满足标准 | OCR + RMA 法规检索 | 提供法规摘要 + 关键词分类 |
| 起草 AEE Report | 撰写结构建议与内容摘要 | 多文档摘要 + 文风迁移 | 提供高质量 AEE 范文语料 |
| 回应 S92 请求 | 自动分配、初步生成回应模板 | 文档分类 + 精准补全 | S92 案例数据库 |

---

## 三、提前准备的关键资产（以语料 + 模板为核心）

- `/aee_samples/`：历史高质量 AEE 报告，结构标注版本优先；
- `/rc_checklist/`：Checklist JSON 标准化格式；
- `/rma_excerpts/`：与 RC 申请相关的 RMA 法规段落摘要；
- `/s92_templates/`：常用 S92 回应语料 + 可复用结构；
- `/planner_workflow/`：整体任务分解结构文档（便于 AI 理解流程）；

---

## 四、人机协作的定义与目标（定义 by Fred）

> **“人机协作的最佳切入点” = 人的关键判断力 + AI 的自动化能力之间的最优分工节点。**

### 【定义】
- AI 负责结构化、重复性、抽象能力强的任务；
- 人保留模糊判断、伦理决策、经验权衡与最终定案；
- 协作目标：**交由 AI 的部分越多越好，但不得削弱人类系统的质量控制力。**

### 【后续方向】
- 接下来 Fred 将补充 PM 视角、全项目流；
- Polaris 将基于 RC Application 工作流构建模块化协作系统；
- AI 模型将根据该模块优化 prompt 构建 + Retrieval 机制。

---

## 五、后续建议与路径

1. Fred 提供至少 3 篇 AEE 报告样本；
2. 整理出一套典型的 RC Checklist（可视化 + JSON 格式）；
3. 构建 `/rc_application_pipeline/` 模块，并分层标注人机分工点；
4. 用 Polaris 的“系统反馈机制”定期检视哪些任务应由 AI 接管；
5. 与 PM 工作流合并，构建“开发项目全过程 AI 协作图谱”。

---

## 附：即将展开的 PM 工作流细化模块（待 Fred 更新）

- 项目启动评估（Site Feasibility）
- 顾问配置与协调机制
- 与开发商/业主沟通决策流程
- Finance / QS / Buildability 分析结构
- Consent 到 Construction 的移交节点
