 
import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import yaml

class StartApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pygame.init()
        # 读取UIConfig.yaml文件
        with open('UI\\UIConfig.yaml', 'r', encoding='utf-8') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)

        # 获取背景图路径
        bg_path = config['WindowsMain']['background']
        # 获取标题
        title = config['WindowsMain']['title']
        # 设置图标
        icon_path = config['WindowsMain']['icon']
        

        # 创建主窗口
        app = QApplication(sys.argv)
        self.setGeometry(0, 0, 960, 512)
        self.setFixedSize(960, 512)
        # 设置标题
        self.setWindowTitle(title)
        # 创建QIcon对象
        icon = QIcon(QPixmap(bg_path))
        # 设置窗口图标
        self.setWindowIcon(icon)

        # 加载背景图
        bg_label = QLabel(self)
        bg_label.setPixmap(QPixmap(bg_path).scaled(960, 512, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
        bg_label.setGeometry(0, 0, 960, 512)

        # 获取屏幕分辨率
        screen = pygame.display.Info()
        screen_width = screen.current_w
        screen_height = screen.current_h

        # 计算缩放比例
        scale_width = screen_width / 1920
        scale_height = screen_height / 1080

        # 根据缩放比例调整窗口大小
        self.setGeometry(0, 0, int(960 * scale_width), int(512 * scale_height))
        self.setFixedSize(int(960 * scale_width), int(512 * scale_height))

         
        # 创建黑色半透明蒙版
        mask = QLabel(self)
        mask.setStyleSheet("background-color: rgba(0, 0, 0, 150);")
        mask.setGeometry(0, 0, self.width(), self.height())
        mask.show()

        # 将浮点数转换为整数
        x = int((screen_width - self.width()) / 2)
        y = int((screen_height - self.height()) / 2)

        # 移动窗口
        self.move(x, y)

        self.show()
        sys.exit(app.exec_())
    

