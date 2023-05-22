
# 系统
import time
import os
import sys
import locale






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
    init()
    # 打印python位置
    # print(sys.executable)
    # print(os.path.dirname(sys.executable))

    from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
    from UI.WindowsMain import StartApp
    app = QApplication(sys.argv)
    start_app = StartApp()
    sys.exit(app.exec_())
    
    

# Only call the main function if this file is being run directly (not imported as a module)
if __name__ == '__main__':
    main()