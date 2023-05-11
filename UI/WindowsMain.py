import yaml
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QVBoxLayout, QLabel, QDialog
from PyQt5.QtGui import QIcon, QPainter, QBrush, QFont
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QRect


def WindowsMain():
    class MyWidget(QWidget):
        def __init__(self):
            super().__init__()

            # 调用方法配置窗口标题和图标
            self.set_title_and_icon()

            # 定义窗口尺寸
            self.width = 1306
            self.height = 760

            # 调用方法设置窗口大小
            self.setFixedSize(self.width, self.height)

            # 初始化进度条并标记为关闭状态
            self.progress = QProgressBar(self)
            self.progress.setGeometry(0, 0, self.width, 50)
            self.progress.setValue(0)
            self.progress.hide()
            
            # 添加一个垂直布局管理器
            layout = QVBoxLayout()

            
        # 定义方法读取并设置标题和图标
        def set_title_and_icon(self):
            with open('UI/UIConfig.yaml', 'r', encoding='utf-8') as f:
                try:
                    config = yaml.safe_load(f)
                    WindowsMainConfig = config.get('WindowsMain')
                    if 'title' in WindowsMainConfig.keys():
                        self.setWindowTitle(WindowsMainConfig.get('title'))
                    else:
                        self.setWindowTitle("弹幕姬")
                    if 'icon' in WindowsMainConfig.keys():
                        self.setWindowIcon(QIcon(WindowsMainConfig.get('icon')))
                    else:
                        pass
                except yaml.YAMLError:
                    print("配置为空或者错误")



    # 创建应用程序实例
    app = QApplication(sys.argv)

    # 创建窗口实例
    window = MyWidget()

    # 显示窗口
    window.show()

    # 进入主循环
    sys.exit(app.exec_())
