import os
import json
import sys
from datetime import datetime

# ==== 基本配置 ====
BASE_PATH = "d:/Dropbox/800-Public/Python/Prj_ai_pm_assets"
TARGET_DIR = os.path.join(BASE_PATH, "99_Core_Registry_and_Tools")
SNAPSHOT_FILE = os.path.join(TARGET_DIR, "last_snapshot.json")
LOG_DIR = os.path.join(TARGET_DIR, "update_logs")

# ==== 获取所有 .md 文件 ====
def get_all_md_files():
    md_files = []
    for root, _, files in os.walk(BASE_PATH):
        for file in files:
            if file.endswith(".md") and "update_log" not in file:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, BASE_PATH).replace("\\", "/")
                md_files.append(rel_path)
    return sorted(md_files)

# ==== 读取快照 ====f
def read_snapshot():
    if os.path.exists(SNAPSHOT_FILE):
        with open(SNAPSHOT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# ==== 写入快照 ====
def write_snapshot(data):
    with open(SNAPSHOT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# ==== 写入 Markdown 日志 ====
def write_update_log(new_files, date):
    date_md = date.strftime("%d%m%y")
    date_title = date.strftime("%Y-%m-%d")
    log_file = os.path.join(LOG_DIR, f"update_log_{date_md}.md")
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"# 📅 更新日誌: {date_title}\n\n")
        f.write(f"## ✅ 今日新增 / 更新 Markdown 文件\n")
        for path in new_files:
            f.write(f"- {path}\n")
        f.write(f"\n## 🧷 相關原始資料\n")
        for path in new_files:
            pdf = os.path.basename(path).replace(".md", ".pdf")
            f.write(f"- {pdf}\n")

# ==== 主函数 ====
def main():
    force = "--force" in sys.argv
    current_files = get_all_md_files()
    previous_files = read_snapshot()
    new_files = [f for f in current_files if f not in previous_files]

    if new_files or force:
        print("[SYNC] 更新中...")
        write_snapshot(current_files)
        write_update_log(new_files if new_files else current_files, datetime.now())
        print(f"[SYNC] ✅ 日誌已生成，共 {len(new_files) if new_files else len(current_files)} 筆。")
    else:
        print("[SYNC] 無變更，未生成日誌。")

if __name__ == "__main__":
    main()