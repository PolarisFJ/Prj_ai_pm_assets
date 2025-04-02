import os
import json
from pathlib import Path

# === 配置参数 ===
project_root = Path(__file__).resolve().parent  # 保持在 99_Core_Registry_and_Tools 目录下
md_folder = project_root.parent / "Prj_ai_pm_assets"
reference_image_dir = Path("D:/Dropbox/001-Ref Library/001-1 Review Station/Note 99-AI Registered Notes & Photos")
output_path = project_root / "reference_registry_autogen.json"

# === 支援的圖像與PDF類型 ===
valid_extensions = {".jpg", ".jpeg", ".png", ".pdf", ".JPG", ".PDF"}

# === 搜索所有 .md 文件 ===
md_files = list(md_folder.rglob("*.md"))

# === 搜索所有参考图片 ===
reference_files = [f for f in reference_image_dir.iterdir() if f.suffix in valid_extensions]

# === 建立映射结构 ===
registry = {}

for md_file in md_files:
    key = md_file.name
    related_refs = []

    for ref in reference_files:
        if key.replace(".md", "") in ref.name:
            related_refs.append({
                "filename": ref.name,
                "type": "image" if ref.suffix.lower() in {".jpg", ".jpeg", ".png"} else "pdf",
                "format": ref.suffix.upper().replace(".", ""),
                "local_path": str(ref),
                "comment": "",
                "added": ""
            })

    if related_refs:
        registry[key] = related_refs

# === 確保目錄存在並寫入 JSON ===
output_path.parent.mkdir(parents=True, exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(registry, f, indent=2, ensure_ascii=False)

print(f"[✅] Reference registry generated: {output_path}")
