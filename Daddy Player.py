from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, QEvent

import mainWin
import sys
from settings import Player, vlc
import time
import getinfo

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,  parent=None):
        super(MainWindow,  self).__init__(parent)
        self.ui = mainWin.Ui_MainWindow()
        self.ui.setupUi(self)
        self.play = Player()
        self.label = QtWidgets.QGraphicsView()
        self.label.showFullScreen()
        self.label.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.play.add_callback(vlc.EventType.MediaPlayerLengthChanged, self.media_lenth)
        self.play.add_callback(vlc.EventType.MediaPlayerPositionChanged, self.refresh_time)


    def roomID(self):
        return self.ui.roomID.text()
    # 播放暂停视频
    def Play(self):
        #addr = getinfo.getLiveAddr(self.roomID())
        self.play.set_ratio("21:9")
        self.label.show()
        self.play.set_handleWin(self.videoWin.winId())
        #self.play.set_handleWin(self.ui.videoWin.winId())
        #self.play.add_callback(vlc.EventType.MediaStateChanged, self.my_callback)
        self.state = self.play.get_state()
        if self.state == 1:
            self.play.pause()
        elif self.state == 0:
            self.play.resume()
        else:
            self.play.play(r"http://tx.hls.huya.com/huyalive/31618642-31618642-135801033333932032-734400720-10057-A-0-1_1200.m3u8")
            #self.play.play(r"https://qqc1107.phpdaniu.com/japan/20191013/TnoqbCFH/500kb/hls/index.m3u8")
            #self.thread.start()
    # 更新播放总时长
    def media_lenth(self, event):
        state = self.play.get_length()
        self.ui.endTime.setText(self.GetLenth(state))

    # 直播信息
    def LiveInfo(self):
        #self.ui.resultText.setText(getinfo.getLiveInfo(1)[0])
        self.rThread = WorkThread()
        self.rThread.trigger.connect(self.display_info)
        self.rThread.start()
    def display_info(self, text):
        self.ui.resultText.setText(text)

    # 更新播放时间
    def refresh_time(self, event):
        self.ui.startTime.setText(self.GetLenth(self.play.media.get_time()))
    # 停止视频
    def Stop(self):
        self.play.resume()
        self.play.stop()
        #self.play.release()


    # 显示视频长度
    def GetLenth(self, point):
        h = str(point // 1000 // 60 // 60 % 60).zfill(2)
        m = str(point // 1000 // 60 % 60).zfill(2)
        s = str(point // 1000 % 60).zfill(2)
        return "{}:{}:{}".format(h, m, s)
    # 检测视频状态
    #def VideoState(self, text):
        # if text == "t":
        #     self.play.resume()
        #     #print(self.play.get_length())

    # 全屏
    def FullScreen(self, QEvent):
        #self.ui.videoWin.setFixedHeight(1080)
        print(1)
class WorkThread(QtCore.QThread):
    trigger = pyqtSignal(str)
    def __init__(self):
        super(WorkThread,  self).__init__()

    def run(self):
        textBox = getinfo.getLiveInfo(1)
        self.trigger.emit("\n\n".join(textBox))








if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())