from pathlib import Path
import os
import json

# === 路径配置 ===
BASE_DIR = Path(__file__).resolve().parent.parent  # 指向 Prj_ai_pm_assets/
TOOLS_DIR = BASE_DIR / "99_Core_Registry_and_Tools"
SNAPSHOT_PATH = TOOLS_DIR / "last_snapshot.json"
REGISTRY_PATH = TOOLS_DIR / "pm_index_registry.md"


def scan_all_markdown_files(base_dir: Path):
    """扫描所有 .md 文件，排除隐藏文件和临时文件"""
    return sorted([
        str(path.relative_to(base_dir)).replace("\\", "/")
        for path in base_dir.rglob("*.md")
        if not path.name.startswith(".") and not path.name.startswith("~")
    ])


def load_snapshot(snapshot_path: Path):
    if snapshot_path.exists():
        with open(snapshot_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_snapshot(snapshot_path: Path, data):
    with open(snapshot_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def update_registry(registry_path: Path, entries):
    with open(registry_path, "w", encoding="utf-8") as f:
        f.write("# 📁 PM Index Registry (Auto Generated)\n\n")
        for entry in entries:
            f.write(f"- [{entry}]({entry})\n")


def main():
    print(f"[SYNC] Base path: {BASE_DIR}")
    print(f"[SYNC] Registry file: {REGISTRY_PATH}")
    print(f"[SYNC] Snapshot file: {SNAPSHOT_PATH}")

    all_md_files = scan_all_markdown_files(BASE_DIR)
    last_snapshot = load_snapshot(SNAPSHOT_PATH)

    if all_md_files != last_snapshot:
        print("[SYNC] Detected changes → updating registry...")
        update_registry(REGISTRY_PATH, all_md_files)
        save_snapshot(SNAPSHOT_PATH, all_md_files)
        print(f"[SYNC] ✅ Updated with {len(all_md_files)} files.")
    else:
        print("[SYNC] No changes detected. Registry is up to date.")


if __name__ == "__main__":
    main()
