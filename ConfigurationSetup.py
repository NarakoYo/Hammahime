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
# 如果不存在弹出一个确认窗口，
# 窗口内提示"本地环境异常，请重新下载压缩包"

 
import os
import subprocess

class ConfigurationSetup:
    def check_venv(self):
        venv_path = os.path.join(os.getcwd(), 'venv')
        if not os.path.exists(venv_path):
            root = tk.Tk()
            root.iconbitmap('image/v50.ico')
            root.withdraw()
            messagebox.showinfo('本地环境异常', '请前往 https://github.com/NarakoYo/Hammahime 重新下载!')
            root.destroy()
            os.system('start https://github.com/NarakoYo/Hammahime')
        else:
            # 使用pip命令更新pip本身到最新版本
            subprocess.call('python -m pip install --upgrade pip', shell=True)
            # 使用pip命令更新setuptools模块到最新版本，setuptools是一个用于打包和分发Python项目的工具
            subprocess.call('python -m pip install --upgrade setuptools', shell=True)
            # 使用pip命令更新wheel模块到最新版本，wheel是一个用于构建和安装Python二进制包的格式和工具
            subprocess.call('python -m pip install --upgrade wheel', shell=True)
            # 使用pip命令强制重新安装requirements.txt文件中指定的模块和版本，requirements.txt是一个包含项目依赖的文件
            subprocess.call('python -m pip install --upgrade --force-reinstall -r requirements.txt', shell=True)
            # 使用pip命令生成一个包含当前安装的模块和版本的新文件requirements_atPresent.txt
            subprocess.call('python -m pip freeze > requirements_atPresent.txt', shell=True)
            # 打开requirements.txt文件，逐行读取内容
            with open('requirements.txt', 'r') as f:
                requirements = f.readlines()
                # 遍历每一行
            for requirement in requirements:
                # 去除空格和换行符
                requirement = requirement.strip()
                # 如果不是空行
                if requirement:
                    # 以==为分隔符，获取模块的名称和版本
                    name, version = requirement.split('==')
                    # 尝试导入该模块
                    try:
                        module = __import__(name)
                         # 如果导入成功，但是版本不匹配
                        if module.__version__ != version:
                            # 使用pip命令安装指定的版本
                            subprocess.call(f'pip install {name}=={version}', shell=True)
                            # 如果导入失败，说明该模块没有安装
                    except ImportError:
                        # 使用pip命令安装指定的版本
                        subprocess.call(f'pip install {name}=={version}', shell=True)
            # 导入tkinter模块，用于创建图形界面
            import tkinter as tk
            from tkinter import messagebox
            # 创建一个根窗口对象，并设置其大小
            root = tk.Tk()
            root.geometry('540x171')
            # 隐藏根窗口，只显示消息框
            root.withdraw()
            # 显示一个消息框，标题为“本地环境正常”，内容为“环境已经准备好”
            messagebox.showinfo('本地环境正常', '环境已经准备好')
            # 销毁根窗口对象，结束程序
            root.destroy()

