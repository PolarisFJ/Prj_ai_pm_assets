
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

# ==== 读取快照 ====
def read_snapshot():
    if os.path.exists(SNAPSHOT_FILE):
        with open(SNAPSHOT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return None  # 用 None 代表首次运行

# ==== 写入快照 ====
def write_snapshot(data):
    with open(SNAPSHOT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# ==== 写入 Markdown 日志 ====
def write_update_log(new_files, all_files, date, is_first_run=False):
    date_md = date.strftime("%d%m%y")
    date_title = date.strftime("%Y-%m-%d")
    time_str = date.strftime("%H:%M:%S")
    log_file = os.path.join(LOG_DIR, f"update_log_{date_md}.md")

    os.makedirs(LOG_DIR, exist_ok=True)

    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"# 📅 更新日誌: {date_title}\n\n")

        f.write("## ✅ 今日新增 / 更新 Markdown 文件\n\n")
        if new_files:
            for path in new_files:
                f.write(f"- {path}\n")
        f.write("\n")

        f.write("## 🧷 相關原始資料\n\n")
        if new_files:
            for path in new_files:
                pdf = os.path.basename(path).replace(".md", ".pdf")
                f.write(f"- {pdf}\n")
        f.write("\n")

        f.write("## 🗒️ 摘要\n\n")
        if is_first_run:
            f.write("- 首次運行，快照已建立，以下為當前系統中所有 Markdown 文件。\n\n")
        f.write("---\n\n")

        f.write(f"✅ Detected and recorded the following `.md` files at {time_str}\n\n")
        for path in all_files:
            f.write(f"- ../{path}\n")

# ==== 主函数 ====
def main():
    force = "--force" in sys.argv
    current_files = get_all_md_files()
    previous_files = read_snapshot()

    # 首次运行，写入快照但不认为任何文件是“新增”
    if previous_files is None:
        print("[INIT] 首次運行：初始化快照，不記錄新增文件。")
        write_snapshot(current_files)
        write_update_log([], current_files, datetime.now(), is_first_run=True)
        return

    new_files = [f for f in current_files if f not in previous_files]

    if new_files or force:
        print("[SYNC] 正在生成更新日誌...")
        write_snapshot(current_files)
        write_update_log(new_files if new_files else [], current_files, datetime.now())
        print(f"[SYNC] ✅ 日誌已生成，共 {len(new_files)} 筆。" if new_files else "[SYNC] ✅ 強制模式：日誌已生成（無新增）。")
    else:
        print("[SYNC] 無變更，未生成日誌。")

if __name__ == "__main__":
    main()
