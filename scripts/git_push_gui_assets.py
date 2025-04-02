# scripts/git_push_gui_assets.py

import subprocess
import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime
import os

# ✅ 设置 Git 仓库路径
repo_path = r"D:\Dropbox\800-Public\Python\Prj_ai_pm_assets"

def is_git_repo(path):
    return os.path.exists(os.path.join(path, ".git"))

def has_changes_to_commit(path):
    result = subprocess.run(["git", "status", "--porcelain"], cwd=path, capture_output=True, text=True, shell=True)
    return result.stdout.strip() != ""

def run_git_command(command_list, path):
    return subprocess.run(command_list, cwd=path, shell=True)

# ✅ 主逻辑开始
if not is_git_repo(repo_path):
    messagebox.showerror("错误", f"❌ 找不到 .git 目录，请确认仓库路径是否正确：\n{repo_path}")
    exit(1)

if not has_changes_to_commit(repo_path):
    messagebox.showinfo("无变更", "✅ 没有可提交的更改，Git 状态正常。")
    exit(0)

# ✅ 弹窗获取提交信息
root = tk.Tk()
root.withdraw()
user_message = simpledialog.askstring("Git 提交", "请输入本次 Git 提交说明：")

if not user_message:
    messagebox.showinfo("取消提交", "⚠️ 已取消：未输入任何说明。")
    exit(0)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
commit_message = f"{user_message} - {timestamp}"

# ✅ 执行 Git 操作
try:
    run_git_command(["git", "add", "."], repo_path)
    commit_result = run_git_command(["git", "commit", "-m", commit_message], repo_path)
    if commit_result.returncode != 0:
        messagebox.showinfo("无提交", "⚠️ Git 没有新增变更可提交。")
        exit(0)
    run_git_command(["git", "push", "origin", "main"], repo_path)
    messagebox.showinfo("提交成功", f"✅ Git 已推送：\n{commit_message}")
except Exception as e:
    messagebox.showerror("错误", f"❌ Git 执行中发生错误：\n{str(e)}")
