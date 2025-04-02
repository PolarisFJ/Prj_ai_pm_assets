import os
import json
from datetime import datetime

# 路徑設置
BASE_PATH = "d:/Dropbox/800-Public/Python/Prj_ai_pm_assets"
REGISTRY_FILE = os.path.join(BASE_PATH, "99_Core_Registry_and_Tools", "pm_index_registry.md")
SNAPSHOT_FILE = os.path.join(BASE_PATH, "99_Core_Registry_and_Tools", "last_snapshot.json")
LOG_DIR = os.path.join(BASE_PATH, "99_Core_Registry_and_Tools", "update_logs")

# 收集所有 .md 檔案
def get_all_md_files(base_path):
    md_files = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, BASE_PATH).replace("\\", "/").replace('"', "'")
                md_files.append(rel_path)
    return sorted(md_files)

# 讀取快照
def read_snapshot():
    if os.path.exists(SNAPSHOT_FILE):
        with open(SNAPSHOT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# 寫入快照
def write_snapshot(data):
    with open(SNAPSHOT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# 更新註冊表
def update_registry(current_files):
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        f.write("# 📁 AI PM 資產登錄總表\n\n")
        for path in current_files:
            f.write(f"- `{path}`\n")

# 寫入簡化格式的每日更新日誌
def write_update_log(new_files):
    if not new_files:
        return
    now = datetime.now()
    date_str = now.strftime("%d%m%y")
    date_display = now.strftime("%Y-%m-%d")
    log_path = os.path.join(LOG_DIR, f"update_log_{date_str}.md")

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(f"# 📅 更新日誌: {date_display}\n\n")

        f.write("## ✅ 今日新增 / 更新 Markdown 文件\n")
        for path in new_files:
            f.write(f"- {path}\n")

        f.write("\n## 🧷 相關原始資料\n")
        for path in new_files:
            pdf_name = os.path.basename(path).replace(".md", ".pdf")
            f.write(f"- {pdf_name}\n")

        f.write("\n## 💬 摘要\n")
        f.write("- （請人工補充說明摘要內容）\n")

# 主程序入口
def main():
    print(f"[SYNC] Base path: {BASE_PATH}")
    current_files = get_all_md_files(BASE_PATH)
    previous_files = read_snapshot()
    new_files = [f for f in current_files if f not in previous_files]

    if new_files:
        print("[SYNC] Detected changes -> updating registry...")
        update_registry(current_files)
        write_snapshot(current_files)
        write_update_log(new_files)
        print(f"[SYNC] ✅ Updated with {len(new_files)} files.")
    else:
        print("[SYNC] No changes detected.")

if __name__ == "__main__":
    main()
