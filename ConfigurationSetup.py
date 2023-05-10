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

# 在windows电脑，启动命令行，检测是否存在虚拟环境venv，
# 如果不存在弹出一个分辨率为540*171的确认窗口，
# 窗口内提示"本地环境异常，请重新下载压缩包"

 
import os
import subprocess
import tkinter as tk
from tkinter import messagebox

def check_venv():
    venv_path = os.path.join(os.getcwd(), 'venv')
    if not os.path.exists(venv_path):
        root = tk.Tk()
        root.iconbitmap('image/v50.ico')
        root.withdraw()
        messagebox.showinfo('本地环境异常', '请前往 https://github.com/NarakoYo/Hammahime 重新下载!')
        root.destroy()
        # os.system('start https://github.com/NarakoYo/Hammahime')
    else:
        activate_path = os.path.join(venv_path, 'Scripts', 'activate.bat')
        subprocess.call(activate_path, shell=True)
        subprocess.call('pip install -r requirements.txt', shell=True)
        subprocess.call('pip freeze > requirements_atPresent.txt', shell=True)
        with open('requirements.txt', 'r') as f:
            requirements = f.readlines()
        for requirement in requirements:
            requirement = requirement.strip()
            if requirement:
                name, version = requirement.split('==')
                try:
                    module = __import__(name)
                    if module.__version__ != version:
                        subprocess.call(f'pip install {name}=={version}', shell=True)
                except ImportError:
                    subprocess.call(f'pip install {name}=={version}', shell=True)
        root = tk.Tk()
        root.geometry('540x171')
        root.withdraw()
        messagebox.showinfo('本地环境正常', '环境已经准备好')
        root.destroy()

check_venv()
