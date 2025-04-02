# 保存为 scripts/git_push_gui_assets.py

import subprocess
import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime
import os

# ✅ 设置 Git 仓库路径（确保为你的 Prj_ai_pm_assets 路径）
repo_path = r"D:\Dropbox\800-Public\Python\Prj_ai_pm_assets"

# ✅ 确保路径是 Git 仓库
if not os.path.exists(os.path.join(repo_path, ".git")):
    messagebox.showerror("错误", f"❌ 找不到 .git 目录，请确认仓库路径是否正确：\n{repo_path}")
    exit(1)

# ✅ GUI 弹窗输入提交说明
root = tk.Tk()
root.withdraw()
user_message = simpledialog.askstring("Git 提交", "请输入本次 Git 提交说明：")

if user_message:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"{user_message} - {timestamp}"

    try:
        subprocess.run(["git", "add", "."], cwd=repo_path, check=True, shell=True)
        subprocess.run(["git", "commit", "-m", commit_message], cwd=repo_path, check=True, shell=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=repo_path, check=True, shell=True)
        messagebox.showinfo("提交成功", f"✅ Git 已推送：\n{commit_message}")
    except subprocess.CalledProcessError:
        messagebox.showerror("错误", "⚠️ Git 执行过程中发生错误，请检查 Git 状态。")
else:
    messagebox.showinfo("取消提交", "⚠️ 已取消：未输入任何说明。")
