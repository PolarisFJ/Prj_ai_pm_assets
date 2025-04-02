# 📁 asset_sync_010425.py Documentation

本文件作为 `asset_sync_010425.py` 脚本的功能说明文档，旨在支持未来的模块复用、自动化系统集成与 AI 协同调用。

---

## 📌 模块作用

自动扫描 `Prj_ai_pm_assets/` 主目录下的 `.md` 文件，生成并更新：

- `pm_index_registry.md`：主索引文档（Markdown格式）
- `last_snapshot.json`：当前结构快照（用于版本追踪）
- `naming_snapshot.json`（可选）：用于追踪文件命名策略和历史变动

---

## 🧱 模块结构

| 函数名 | 功能描述 |
|--------|----------|
| `scan_md_files(directory)` | 遍历给定目录及子目录下所有 `.md` 文件，返回相对路径列表 |
| `load_snapshot(snapshot_path)` | 加载历史快照（JSON），用于对比 |
| `compare_snapshots(current, previous)` | 对比当前扫描结果与历史快照，找出新增与移除项 |
| `write_snapshot(snapshot_path, data)` | 写入当前快照 |
| `generate_index_markdown(md_files)` | 基于 `.md` 文件路径生成结构化 Markdown 索引内容 |
| `write_index_file(index_path, content)` | 写入 `pm_index_registry.md` 文件 |

---

## 🔗 文件交互关系图

```
Prj_ai_pm_assets/
├── pm_index_registry.md  ⬅️ 主输出文件
├── last_snapshot.json     ⬅️ 快照，用于差异比较
├── naming_snapshot.json   ⬅️ 命名追踪（可选）
└── 各阶段目录（Due Diligence、RC、EPA & BC、Construction...）
```

---

## 🧠 AI 模块调用建议

- 可以通过关键函数 `generate_index_markdown()` 输出 Markdown 内容，用于自动汇报、目录同步等功能。
- 若未来集成至 CLI 或网页工具，推荐将 `compare_snapshots()` 的差异直接渲染为 UI 提醒。
- 可与 `asset_snapshot_viewer.py` 等可视化工具协同使用。

---

## 🪢 注意事项

- 脚本默认快照文件路径为项目根目录中的 `last_snapshot.json`，如有多个版本需指定路径。
- 如有文件名变更，建议使用 `naming_snapshot.json` 来追踪历史命名逻辑。
- 结构更新后建议执行 Git 提交，保持历史可追溯性。

---

## 📅 当前版本

版本代号：`asset_sync_010425`
更新时间：由系统自动记录
