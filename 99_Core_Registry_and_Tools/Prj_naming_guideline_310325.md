
# Prj_naming_guideline.md

本文件為 AI PM Assets 專案命名規則總綱，用於指導 Markdown 文件、圖片、索引等資產命名，以利後續檔案管理、自動同步與 AI 調用。

---

## ✅ 命名組成原則

```
[分類縮寫]_[主題名稱]_[日期].md
```

### 範例：
- RC_LandscapeReview_310325.md
- EPA_StormwaterCheck_050424.md

---

## ✅ 日期格式（更新於 2025-03-31）

- 採用格式：`DDMMYY`（日月年，例：310325 表示 2025年3月31日）
- 理由：
  - 更符合人腦閱讀邏輯（先看日期與月份）
  - 檔名預覽簡潔（節省空間）
  - 支援日常人工分類與快速搜尋

---

## ✅ 分類縮寫建議對照表

| 縮寫 | 說明 |
|------|------|
| RC   | Resource Consent 階段 |
| BC   | Building Consent 階段 |
| EPA  | Environmental Protection Assessment |
| CON  | Construction（現場執行）階段 |
| PM   | Project Management 通用記錄 |
| REG  | Registration / Index / Naming Guideline |

---

## ✅ 命名補充建議

- 若為同一主題的更新版本，可於主題後附 `v2`, `v3` 等版本標記：
  - 範例：`RC_LandscapeReview_310325_v2.md`
- 所有模板文件應明確標示為 `md_template`，如：
  - `AI_PM_Assets_md_template_v2_310325.md`

---

本規則將由 AI 自動化系統（asset_sync.py）參考與檢查，所有新加入 `.md` 文件建議遵循本命名結構以確保一致性與可追溯性。
