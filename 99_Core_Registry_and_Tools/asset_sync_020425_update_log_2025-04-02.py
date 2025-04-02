
import os
import json
from datetime import datetime

BASE_PATH = "d:\\Dropbox\\800-Public\\Python\\Prj_ai_pm_assets"
REGISTRY_FILE = os.path.join(BASE_PATH, "99_Core_Registry_and_Tools", "pm_index_registry.md")
SNAPSHOT_FILE = os.path.join(BASE_PATH, "99_Core_Registry_and_Tools", "last_snapshot.json")
UPDATE_LOG_DIR = os.path.join(BASE_PATH, "99_Core_Registry_and_Tools", "update_logs")

def list_md_files(base_path):
    md_files = []
    for root, _, files in os.walk(base_path):
        for f in files:
            if f.endswith(".md") and "update_logs" not in root:
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, os.path.join(BASE_PATH, "Prj_ai_pm_assets")).replace('\\', '/')
                md_files.append(rel_path)
    return sorted(md_files)

def load_snapshot():
    if os.path.exists(SNAPSHOT_FILE):
        with open(SNAPSHOT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_snapshot(data):
    with open(SNAPSHOT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def update_registry(file_list):
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        for path in file_list:
            f.write(f"- [{path}]({path})\n")

def create_update_log(file_list):
    today_str = datetime.now().strftime("update_log_%Y-%m-%d.md")
    log_path = os.path.join(UPDATE_LOG_DIR, today_str)
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(f"# 📘 Update Log ({today_str})\n\n")
        f.write(f"✅ Detected and recorded the following `.md` files at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for path in file_list:
            f.write(f"- {path}\n")

def main():
    print(f"[SYNC] Base path: {BASE_PATH}")
    current_files = list_md_files(BASE_PATH)
    old_snapshot = load_snapshot()

    if current_files != old_snapshot:
        print("[SYNC] Detected changes -> updating registry...")
        update_registry(current_files)
        save_snapshot(current_files)
        create_update_log(current_files)
        print(f"[SYNC] ✅ Updated with {len(current_files)} files.")
    else:
        print("[SYNC] No changes detected.")

if __name__ == "__main__":
    main()
