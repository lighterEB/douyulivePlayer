from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

# 创建一个应用实例
app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle('H5播放器')

# 创建一个垂直布局
layout = QVBoxLayout()
win.setLayout(layout)

# 创建一个QWebEngineView 对象
view = QWebEngineView()
view.setHtml('''
<div id="player1" class="dplayer"></div>
<!-- ... -->
<script src="DPlayer.min.js"></script>

''')

# 创建一个调用按钮
button = QPushButton('开始')

def js_callback(result):
    print(result)

def complete_name():
    view.page().runJavaScript('aaa();', js_callback)

button.clicked.connect(complete_name)

layout.addWidget(view)
win.show()
sys.exit(app.exec_())