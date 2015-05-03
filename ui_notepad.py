# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notepad.ui'
#
# Created: Sat Mar 16 16:05:10 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Notepad(object):
    def setupUi(self, Notepad):
        Notepad.setObjectName(_fromUtf8("Notepad"))
        Notepad.resize(629, 451)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/notepad.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Notepad.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Notepad)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        Notepad.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Notepad)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 629, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.fileMenu = QtGui.QMenu(self.menubar)
        self.fileMenu.setObjectName(_fromUtf8("fileMenu"))
        self.helpMenu = QtGui.QMenu(self.menubar)
        self.helpMenu.setObjectName(_fromUtf8("helpMenu"))
        Notepad.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Notepad)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Notepad.setStatusBar(self.statusbar)
        self.openAction = QtGui.QAction(Notepad)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openAction.setIcon(icon1)
        self.openAction.setObjectName(_fromUtf8("openAction"))
        self.saveAction = QtGui.QAction(Notepad)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveAction.setIcon(icon2)
        self.saveAction.setObjectName(_fromUtf8("saveAction"))
        self.exitAction = QtGui.QAction(Notepad)
        self.exitAction.setObjectName(_fromUtf8("exitAction"))
        self.usageAction = QtGui.QAction(Notepad)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.usageAction.setIcon(icon3)
        self.usageAction.setObjectName(_fromUtf8("usageAction"))
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.helpMenu.addAction(self.usageAction)
        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.helpMenu.menuAction())

        self.retranslateUi(Notepad)
        QtCore.QMetaObject.connectSlotsByName(Notepad)

    def retranslateUi(self, Notepad):
        Notepad.setWindowTitle(QtGui.QApplication.translate("Notepad", "记事本", None, QtGui.QApplication.UnicodeUTF8))
        self.fileMenu.setTitle(QtGui.QApplication.translate("Notepad", "文件(&F)", None, QtGui.QApplication.UnicodeUTF8))
        self.helpMenu.setTitle(QtGui.QApplication.translate("Notepad", "帮助(&H)", None, QtGui.QApplication.UnicodeUTF8))
        self.openAction.setText(QtGui.QApplication.translate("Notepad", "打开(&O)", None, QtGui.QApplication.UnicodeUTF8))
        self.openAction.setStatusTip(QtGui.QApplication.translate("Notepad", "打开文件", None, QtGui.QApplication.UnicodeUTF8))
        self.openAction.setShortcut(QtGui.QApplication.translate("Notepad", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAction.setText(QtGui.QApplication.translate("Notepad", "保存(&S)", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAction.setStatusTip(QtGui.QApplication.translate("Notepad", "保存文件", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAction.setShortcut(QtGui.QApplication.translate("Notepad", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.exitAction.setText(QtGui.QApplication.translate("Notepad", "退出(&X)", None, QtGui.QApplication.UnicodeUTF8))
        self.exitAction.setStatusTip(QtGui.QApplication.translate("Notepad", "退出", None, QtGui.QApplication.UnicodeUTF8))
        self.usageAction.setText(QtGui.QApplication.translate("Notepad", "手册(&H)", None, QtGui.QApplication.UnicodeUTF8))
        self.usageAction.setStatusTip(QtGui.QApplication.translate("Notepad", "使用手册", None, QtGui.QApplication.UnicodeUTF8))
        self.usageAction.setShortcut(QtGui.QApplication.translate("Notepad", "F1", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
