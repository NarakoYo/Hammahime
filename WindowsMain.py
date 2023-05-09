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
            
            # 添加底部显示框
            self.bottom_box = QWidget(self)
            
            # 添加一个垂直布局管理器
            layout = QVBoxLayout()
            
            # 添加一个标签
            label = QLabel("底部显示框的内容")
            layout.addWidget(label)
            
            # 将垂直布局管理器添加到底部显示框中
            self.bottom_box.setLayout(layout)

            # 显示区域比例更改为9：4
            bottom_box_width = int(self.height * 9 / 4 - 24)
            bottom_box_height = int(self.height - 24)

            self.bottom_box.setGeometry(12, self.height - bottom_box_height - 12, bottom_box_width, bottom_box_height)

            # 显示区域四角做圆角处理
            self.bottom_box.setAttribute(Qt.WA_TranslucentBackground)
            # 修改此处，使显示区域底色透明
            self.bottom_box.setStyleSheet("background-color: rgba(0, 0, 0, 0); border-radius: 5px;")

        # 定义方法读取并设置标题和图标
        def set_title_and_icon(self):
            with open('config.yaml', 'r') as f:
                try:
                    config = yaml.safe_load(f)
                    if 'title' in config.keys():
                        self.setWindowTitle(config['title'])
                    else:
                        self.setWindowTitle("弹幕姬")
                    if 'icon' in config.keys():
                        self.setWindowIcon(QIcon(config['icon']))
                    else:
                        pass
                except yaml.YAMLError:
                    print("配置为空或者错误")

        # 修改此处，关闭进度条的方法改为弹出窗口
        def on_close(self, event):
            # 创建进度条窗口实例
            dialog = QDialog(self)
            # 将进度条窗口大小设置为380*120，置顶窗口
            dialog.setFixedSize(380, 120)
            dialog.setWindowFlags(Qt.WindowStaysOnTopHint)

            # 在进度条窗口中添加进度条和文本
            progress = QProgressBar(dialog)
            # 设置进度条最大值为100，进度条颜色为绿色
            progress.setMaximum(100)
            progress.setStyleSheet("QProgressBar::chunk {background-color: #1faa00;}")
            # 设置进度条的位置为垂直左右居中，已知进度条大小为360*25
            progress.setGeometry((dialog.width() - 360) // 2, (dialog.height() - 25) // 2, 360, 25)
            
            # 设置进度条文本
            text = QLabel(dialog)
            text.setAlignment(Qt.AlignCenter)
            font = QFont()
            font.setPointSize(10)
            text.setFont(font)
            # 设置文本大小为360*25，位置紧贴着进度条显示文案“关闭中...”
            # 修改此处，将文本位置设置在进度条之上，位置居中
            text.setGeometry((dialog.width() - 360) // 2, progress.y() - 35, 360, 25)
            text.setText("关闭中...")
            
            # 显示进度条窗口
            dialog.exec_()

        # 定义定时器事件
        def timerEvent(self, event):
            self.step += 1
            self.progress.setValue(self.step)
            if self.step >= 100:
                self.timer.stop()


    # 创建应用程序实例
    app = QApplication(sys.argv)

    # 创建窗口实例
    window = MyWidget()

    # 显示窗口
    window.show()

    # 进入主循环
    sys.exit(app.exec_())
