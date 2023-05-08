import yaml
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal

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
        # 注册关闭事件
        self.closeEvent = self.on_close
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
    # 定义关闭事件的方法
    def on_close(self, event):
        # 显示进度条
        self.progress.show()
        # 定义关闭进度条的方法
        def close_bar():
            self.progress.setValue(self.progress.value() + 1)
            if self.progress.value() >= 100:
                timer.stop()
                print("窗口关闭")
                app.exit()
        # 定义定时器
        timer = QBasicTimer()
        self.step = 0
        # 启动定时器
        timer.start(30, self)
        # 启动进度条
        self.progress.setMaximum(100)
        self.progress.setValue(0)
        while self.progress.value() < 100:
            close_bar()
        # 阻塞主线程直到进度条结束
        app.exec_()
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
