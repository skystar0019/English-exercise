import os
import subprocess

# PyInstaller 的完整路径
pyi_path = r"C:\Users\hello\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts\pyinstaller.exe"
# 你的脚本路径
script_path = "英语复习器.py"

print("正在启动打包...")
try:
    # 调用 PyInstaller 打包
    subprocess.run([pyi_path, "-F", script_path], check=True)
    print("✅ 打包成功！可执行文件在 dist 文件夹里")
except subprocess.CalledProcessError as e:
    print(f"❌ 打包失败，错误信息：{e}")
except FileNotFoundError:
    print(f"❌ 找不到 PyInstaller，请检查路径：{pyi_path}")
input("按回车键关闭窗口...")