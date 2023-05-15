 
import sys
import pygame
import yaml
import gc
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QLabel, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QProgressBar
from PyQt5.QtCore import QThread
from PyQt5.QtCore import QPropertyAnimation, QAbstractAnimation



# 菜单栏
class MenuBar(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        # 读取UIConfig.yaml文件
        with open('UI\\UIConfig.yaml', 'r', encoding='utf-8') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)

        # 获取菜单栏的optionList
        option_list = config['menu']['optionList']

        # 设置菜单栏的位置和大小
        self.setGeometry(10, 10, self.parent.width() - 20, 64)

        # 设置菜单栏的圆角
        self.setStyleSheet("border-radius: 20px;")

        # 设置菜单栏的背景颜色
        self.setStyleSheet("background-color: #FFFFFF;")

        # 设置菜单栏的边框
        self.setStyleSheet("border: 1px solid rgba(0, 0, 0, 0.5);")

        # 设置菜单栏的选项
        for i, option in enumerate(option_list):
            # 创建选项
            option_label = QLabel(self)
            option_label.setGeometry(10 + i * 130, 1, 128, 62)

            # 设置选项的圆角
            option_label.setStyleSheet("border-radius: 16px;")

            # 设置选项的背景颜色
            option_label.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);")

            # 设置选项的边框
            option_label.setStyleSheet("border: 1px solid rgba(255, 255, 255, 0.5);")

            # 获取选项的文本
            print(option_list.get(i))
            option_text = option_list[i]

            # 创建文本标签
            text_label = QLabel(option_label)
            text_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            text_label.setGeometry(0, 0, option_label.width(), option_label.height())

            # 设置文本标签的字体
            font = text_label.font()
            font.setPointSize(16)
             
            #联系上下文设置字体颜色为白色粗字，可根据配置选择字体
            font.setBold(True)
            text_label.setStyleSheet("color: #FFFFFF;")

            text_label.setFont(font)

            # 计算文本标签的缩放比例
            text_width = text_label.fontMetrics().boundingRect(option_text).width()
            text_scale = min(1, option_label.width() / text_width)

            # 根据缩放比例调整文本标签的字体大小
            font_size = int(font.pointSize() * text_scale)
            font.setPointSize(font_size)
            text_label.setFont(font)

            # 设置文本标签的文本
            text_label.setText(option_text)



        # 设置菜单栏的滑动效果
        self.timer = QTimer()
        self.timer.timeout.connect(self.slide)
        self.timer.start(2500)

    def slide(self):
        # 获取菜单栏的位置和大小
        x = self.x()
        y = self.y()
        width = self.width()
        height = self.height()

        # 获取菜单栏的选项
        option_list = self.findChildren(QLabel)

        # 计算选项的总宽度
        option_width = len(option_list) * 66 - 1

        # 如果选项的总宽度小于菜单栏的宽度，则不需要滑动
        if option_width <= width:
            return

        # 计算滑动的距离
        dx = width - option_width

        # 创建动画
        animation = QPropertyAnimation(self, b"geometry")
        animation.setDuration(1000)
        animation.setStartValue(QRect(x, y, width, height))
        animation.setEndValue(QRect(x + dx, y, width, height))
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def mousePressEvent(self, event):
        # 记录鼠标按下的位置
        self.mouse_press_pos = event.pos()

    def mouseMoveEvent(self, event):
        # 计算鼠标移动的距离
        dx = event.pos().x() - self.mouse_press_pos.x()

        # 获取菜单栏的位置和大小
        x = self.x()
        y = self.y()
        width = self.width()
        height = self.height()

        # 获取菜单栏的选项
        option_list = self.findChildren(QLabel)

        # 计算选项的总宽度
        option_width = len(option_list) * 66 - 2

        # 如果选项的总宽度小于菜单栏的宽度，则不需要滑动
        if option_width <= width:
            return

        # 计算滑动的距离
        new_x = x + dx
        if new_x > 10:
            new_x = 10
        if new_x < width - option_width - 10:
            new_x = width - option_width - 10

        # 移动菜单栏
        self.setGeometry(new_x, y, width, height)

    def mouseReleaseEvent(self, event):
        # 清空鼠标按下的位置
        self.mouse_press_pos = None



class StartApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    # UI
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
         
        # 隐藏窗口最大化按钮
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)

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
        mask.setStyleSheet("background-color: rgba(0, 0, 0, 0.4);")
        mask.setGeometry(0, 0, self.width(), self.height())
        mask.show()

        # 将浮点数转换为整数
        x = int((screen_width - self.width()) / 2)
        y = int((screen_height - self.height()) / 2)

        # 移动窗口
        self.move(x, y)

        # 创建菜单栏
        menu_bar = MenuBar(self)
        menu_bar.show()


        # 显示窗口
        self.show()
        sys.exit(app.exec_())

    # 关闭
    def closeEvent(self, event):
        # 创建后台关闭进度条
        progress_bar = QProgressBar(self)
        progress_bar.setGeometry(0, 0, self.width(), 10)
        progress_bar.setStyleSheet("QProgressBar {border: 1px solid gray;border-radius: 5px;background-color: white;}QProgressBar::chunk {background-color: #CD96CD;width: 10px;}")
        progress_bar.show()

        # 获取程序相关后台
        backends = self.findChildren(QThread)

        # 关闭程序相关后台
        for backend in backends:
            backend.quit()

        # 设置进度条走完的动画
        animation = QPropertyAnimation(progress_bar, b"value")
        animation.setDuration(2000)  # 设置进度条最低走完时间为2秒
        animation.setStartValue(0)
        animation.setEndValue(100)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

        # 关闭所有窗口
        for widget in QApplication.topLevelWidgets():
            widget.close()

        # 优化程序相关后台内存利用率
        gc.collect()

        # 关闭程序
        event.accept()



