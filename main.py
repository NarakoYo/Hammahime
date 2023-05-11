
# 系统
import time
import os
import sys
import locale

from UI.WindowsMain import WindowsMain

# Create an initialization function
def init():

    # locale.setlocale(locale.LC_ALL, 'zn_ch.UTF-8')
    # Add initialization code here
    # config = ConfigurationSetup()
    # config.check_venv()

    pass

# 入口
# Define the main function
def main():

    # 初始化
    # init()
    # 打印python位置
    # print(sys.executable)
    # print(os.path.dirname(sys.executable))
    windowsMain = WindowsMain()
    windowsMain.run()



# Only call the main function if this file is being run directly (not imported as a module)
if __name__ == '__main__':
    main()