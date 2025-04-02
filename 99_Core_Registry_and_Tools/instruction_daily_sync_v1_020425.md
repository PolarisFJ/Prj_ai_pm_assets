
# 《每日 AI 协作知识更新流程》Instruction Sheet v1.0

> 目标：确保你每日新增的资料（Markdown/PDF/JPG）**被结构化记录、被 AI 正确索引并纳入长期语义体系中**。

---

## ✅ Step 1：准备资料
**目的：输入当天要整理的新资料内容**

1. 收集当日新增的内容（可能来源）：
   - 项目流程图、会议记录、规范说明
   - 截图 JPG / PDF 流程图 / 文字说明
   - ChatGPT 对话摘要 / AI 输出

2. 将资料通过下列方式之一交给 AI 助手：
   - 直接拖入 ChatGPT 窗口（JPG / PDF / Markdown）
   - 或贴入原始文字 + 简要说明

---

## ✅ Step 2：AI 输出 Markdown 文档
**目的：将碎片资料结构化成 AI 可索引的 Markdown 文件**

3. 由 AI 整理生成 `.md` 文档：
   - 命名规则：`主题名称_日期编号.md`（如 `RC_application_review_020425.md`）
   - 文档中应标注原始文件路径引用（PDF / JPG）

4. 你下载 `.md` 文件并手动放入对应路径：
   - 项目路径：`Prj_ai_pm_assets/`
   - 结构遵循已有模块体系（如 2_RC_Application、4_Civil_Construction 等）

---

## ✅ Step 3：运行 Python 同步脚本
**目的：更新注册索引与快照**

5. 打开 VS Code 终端，运行以下命令：

```
python d:\Dropbox\800-Public\Python\Prj_ai_pm_assets\99_Core_Registry_and_Tools\asset_sync_010425.py
```

6. 检查终端输出：
   - 出现 `[SYNC] ✅ Updated with X files` 表示成功更新
   - 如果无变化，也会提示 `[SYNC] No changes detected`

---

## ✅ Step 4：校验快照与索引
**目的：确保系统状态正确记录**

7. 打开以下文件检查是否同步成功：

   - `last_snapshot.json`：
     - 文件路径应包含新加入的 `.md` 文件
     - 路径格式应正确（如 `"2_RC_Application/RC_flowchart_20250331.md"`）

   - `pm_index_registry.md`：
     - 应看到新文件已归类在相应模块目录下
     - 命名与引用路径无误

---

## ✅ Step 5（可选）：记录操作日志
**目的：便于未来追踪操作历史、时间节点与内容变化**

8. 打开（或建立）一个每日日志 Markdown 文档，例如：

```
📅 DailySync_20250402.md
```

9. 记录以下内容（可复制模板）：

```markdown
## ✅ Daily AI Sync Log - 2025/04/02

### 新增文件：
- RC_application_review_020425.md
- DetentionTank_Install_280325.md

### 操作流程：
- Markdown 文件已手动放入对应文件夹
- Python 脚本运行成功，已更新索引
- 快照文件 last_snapshot.json 已同步
- pm_index_registry.md 内容正确

### 特别备注：
- 今日新增 PDF 流程图共 2 份，已同步标注于 MD 文件尾部
```

---

## ✅ Step 6（每周建议）：整理优化
**目的：优化结构、合并碎片，提升系统稳定性**

- 检查是否有命名不统一的 `.md` 文件
- 检查是否遗漏 PDF/JPG 的引用
- 每周运行一次 `reference_register.py` 等脚本（可后续完善）

---

## ✅ 附加建议：未来可迭代优化

| 方向 | 说明 |
|------|------|
| 自动压缩截图 | 脚本中可增加 JPG 压缩步骤，节省空间 |
| 智能命名建议 | 后续可加入智能命名器，根据语义自动命名 |
| 推送 Git | 每次更新完后可自动推送至 Git 仓库，形成版本管理体系 |

