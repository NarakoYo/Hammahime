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
import sys
import subprocess
import webbrowser

def check_venv():
    if sys.platform == 'win32':
        venv_path = os.path.join(os.getcwd(), 'venv')
        if not os.path.exists(venv_path):
            subprocess.run(['python', '-m', 'venv', 'venv'])
        else:
            activate_path = os.path.join(venv_path, 'Scripts', 'activate.bat')
            if os.path.exists(activate_path):
                subprocess.run([activate_path, '&', 'python', '-m', 'pip', 'install', '-r', 'requirements.txt'])
            else:
                print('activate.bat not found in venv/Scripts')
                return
        subprocess.run(['python', '-m', 'pip', 'freeze', '>', 'requirements_atPresent.txt'])
        with open('requirements.txt', 'r') as f:
            required_modules = f.readlines()
        for module in required_modules:
            module = module.strip()
            if module:
                module_name, module_version = module.split('==')
                try:
                    subprocess.run([activate_path, '&', 'python', '-m', 'pip', 'show', module_name])
                except subprocess.CalledProcessError:
                    subprocess.run([activate_path, '&', 'python', '-m', 'pip', 'install', module])
                else:
                    installed_version = subprocess.check_output([activate_path, '&', 'python', '-m', 'pip', 'show', module_name, '|', 'findstr', 'Version']).decode('utf-8').strip().split(': ')[1]
                    if installed_version != module_version:
                        subprocess.run([activate_path, '&', 'python', '-m', 'pip', 'install', module])
        python_version = subprocess.check_output([activate_path, '&', 'python', '-V']).decode('utf-8').strip()
        installed_modules = subprocess.check_output([activate_path, '&', 'python', '-m', 'pip', 'freeze']).decode('utf-8').strip().split('\n')
        print('当前使用的Python版本为：', python_version)
        print('已安装的模块库有：')
        for module in installed_modules:
            print(module)
        webbrowser.open('https://github.com/NarakoYo/Hammahime')



