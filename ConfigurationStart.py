# 在windows电脑，启动命令行，
# 检测是否存在虚拟环境venv，
# 如果不存在则创建虚拟环境venv，如果存在虚拟环境venv则检测虚拟环境的运行状态，
# 如果正在运行则重启虚拟环境，激活进入虚拟环境，
# 下载安装requirements.txt文件内列出的模块库到虚拟环境，
# 如果虚拟环境已经安装运行了文件内列出的所有模块库，
# 则检测已安装运行的库的版本与requirements.txt文件内的版本是否一致，
# 如果已安装的库版本低于文件内模块版本，则进行更新模块，
# 已安装的库版本高于文件内模块版本，则无需操作。
# 并返回当前所使用的python版本和已安装所有模块库的名字和版本，格式为”模块库名字=版本号“，
# 并使用pip freeze命令写入到requirements_atPresent.txt文件中
# 如果不存在requirements.txt文件，抛出错误，
# 并弹出一个分辨率为540*171的确认窗口，
# 窗口没有关闭等按钮，只存在一个确认按钮，
# 文本居中提示用户"requirements.txt文件缺失，请重新现在压缩包"。
# 当用户点击确认，关闭弹窗。
# 然后打开电脑默认浏览器，前往https://github.com/NarakoYo/Hammahime





import os
import subprocess
import sys
import tkinter as tk
import webbrowser

def check_venv():
    # 检测是否存在虚拟环境venv
    if not os.path.exists("venv"):
        # 如果不存在则创建虚拟环境venv
        subprocess.run(["python", "-m", "venv", "venv"])
    # 如果存在虚拟环境venv则检测虚拟环境的运行状态
    else:
        # 检测虚拟环境是否在运行
        result = subprocess.run(["python", "-c", "import sys; print('running' if hasattr(sys, 'real_prefix') else 'not running')"], capture_output=True, text=True)
        if result.stdout.strip() == "running":
            # 如果正在运行则重启虚拟环境
            subprocess.run(["venv\\Scripts\\activate.bat", "&&", "python", "-m", "pip", "install", "--upgrade", "pip"])
        else:
            # 激活进入虚拟环境
            subprocess.run(["venv\\Scripts\\activate.bat"])

def install_requirements():
    # 下载安装requirements.txt文件内列出的模块库到虚拟环境
    subprocess.run(["python", "-m", "pip", "install", "-r", "requirements.txt"])

def check_installed_modules():
    # 获取已安装的模块库信息
    result = subprocess.run(["python", "-m", "pip", "freeze"], capture_output=True, text=True)
    installed_modules = result.stdout.strip().split("\n")
    installed_modules_dict = {}
    for module in installed_modules:
        name, version = module.split("==")
        installed_modules_dict[name] = version
    # 检测已安装运行的库的版本与requirements.txt文件内的版本是否一致
    with open("requirements.txt", "r") as f:
        required_modules = f.read().strip().split("\n")
    for module in required_modules:
        name, version = module.split("==")
        if name not in installed_modules_dict:
            # 如果虚拟环境已经安装运行了文件内列出的所有模块库，则检测已安装运行的库的版本与requirements.txt文件内的版本是否一致
            print(f"{name}={version}")
        elif installed_modules_dict[name] < version:
            # 如果已安装的库版本低于文件内模块版本，则进行更新模块
            subprocess.run(["python", "-m", "pip", "install", "--upgrade", name])
        elif installed_modules_dict[name] > version:
            # 已安装的库版本高于文件内模块版本，则无需操作
            pass

def write_requirements_atPresent():
    # 在虚拟环境执行pip freeze > requirements_atPresent.txt命令
    subprocess.run(["python", "-m", "pip", "freeze", ">", "requirements_atPresent.txt"], shell=True)

def check_requirements_file():
    # 如果不存在requirements.txt文件，抛出错误
    if not os.path.exists("requirements.txt"):
        # 弹出一个分辨率为540*171的确认窗口，窗口没有关闭等按钮，只存在一个确认按钮，文本居中提示用户"requirements.txt文件缺失，请重新现在压缩包"
        root = tk.Tk()
        root.title("错误")
        root.geometry("540x171")
        root.resizable(False, False)
        tk.Label(root, text="requirements.txt文件缺失，请重新下载压缩包", font=("微软雅黑", 14)).pack(pady=30)
        tk.Button(root, text="确认", font=("微软雅黑", 14), command=root.destroy).pack(pady=20)
        root.focus_set()
        root.mainloop()
        # 限制用户无法操作其他窗口
        sys.exit()

def open_github():
    # 打开电脑默认浏览器，前往https://github.com/NarakoYo/Hammahime
    webbrowser.open("https://github.com/NarakoYo/Hammahime")

check_venv()
check_requirements_file()
install_requirements()
check_installed_modules()
write_requirements_atPresent()
open_github()
