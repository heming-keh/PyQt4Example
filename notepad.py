# coding=utf-8

import sys
import os

from PyQt4.QtGui import QApplication, QMainWindow, QFileDialog
# 设计器中QMainWindow的对象名称是Notepad，导入类就是Ui_Notepad
from ui_notepad import Ui_Notepad


class Notepad(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Notepad, self).__init__(*args, **kwargs)

        # 关键的一步
        self.ui = Ui_Notepad()
        self.ui.setupUi(self)

        # 这里的lambda相当于适配器，以适应closeEvent的参数个数
        self.ui.exitAction.triggered.connect(lambda : self.closeEvent(None))

        # triggered是QAction的信号，与QPushButton的clicked一样
        self.ui.openAction.triggered.connect(self.openFile)
        self.ui.saveAction.triggered.connect(self.saveFile)

        self.ui.usageAction.triggered.connect(lambda : os.startfile(u'help.chm'))


    '''
    #以这种方式来实现的信号链接，会调用两次，估计是bug，暂时不使用这种方法
    def on_openAction_triggered(self):
        print u'on_openAction_triggered'
        # TODO 打开文件

    def on_saveAction_triggered(self):
        print u'on_saveAction_triggered'
        # TODO 保存文件'''

    def openFile(self):
        print u'打开文件'

    def saveFile(self):
        print u'保存文件'

    def closeEvent(self, evt):
        # TODO 退出程序前可以做一些必要的动作，例如保存配置等等
        print u'退出程序'
        sys.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    notepad = Notepad()
    notepad.show()
    sys.exit(app.exec_())
