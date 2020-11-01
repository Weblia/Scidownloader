# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scidownload_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import lxml.etree
import re
from tkinter import filedialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget       #一个是程序，一个是窗口
import sys
from design import scidownload_gui


def load_pmid(file_path):
    f = open(file_path, 'r')
    empty_list = list(f)
    full_list = []
    n = 0
    for i in empty_list:
        full_list.append(i.rstrip())
        n = n + 1
        print(n)
    print(full_list)
    print('共' + n + '篇文献')
    f.close()
    return full_list


def import_pmid_list(self):
    global pmid_list
    Fpath = filedialog.askopenfilename()
    print(Fpath)
    data = {  # 先完善表单内容
        'request': 'undefined'
    }
    pmid_list = self.load_pmid(Fpath)
    print(pmid_list)
    self.textEdit.setPlainText('678')


def change_dir():
    print('change_dir')


def start_download():
    print('start_download')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1084, 817)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(261, 361, 361, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 110, 571, 220))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.widget1)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.listView = QtWidgets.QListView(self.widget1)
        self.listView.setObjectName("listView")
        self.horizontalLayout_2.addWidget(self.listView)
        self.listView_2 = QtWidgets.QListView(self.widget1)
        self.listView_2.setObjectName("listView_2")
        self.horizontalLayout_2.addWidget(self.listView_2)
        self.verticalLayout_2.addWidget(self.splitter)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(51, 358, 181, 111))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(260, 430, 329, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1084, 26))
        self.menubar.setObjectName("menubar")
        self.menuSCI = QtWidgets.QMenu(self.menubar)
        self.menuSCI.setObjectName("menuSCI")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar.addAction(self.menuSCI.menuAction())
        self.retranslateUi(MainWindow)
        #开始设置连接
        self.pushButton.clicked.connect(self.start_download)
        self.pushButton_2.clicked.connect(self.import_pmid_list)
        self.pushButton_3.clicked.connect(self.change_dir)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "待下载文献"))
        self.label_2.setText(_translate("MainWindow", "已下载文献"))
        self.label_3.setText(_translate("MainWindow", "下载失败"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "开始下载"))
        self.pushButton_2.setText(_translate("MainWindow", "导入PMID列表"))
        self.pushButton_3.setText(_translate("MainWindow", "修改下载路径"))
        self.menuSCI.setTitle(_translate("MainWindow", "SCI批量下载工具"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

if __name__ == "__main__":
    # 创建一个app实例
    app = QApplication(sys.argv)
    # 建立一个主窗口
    mymainWindow = QMainWindow()
    # 创建UI
    myui = scidownload_gui.Ui_MainWindow()
    # 将UI应用于生成的主窗口
    myui.setupUi(mymainWindow)
    mymainWindow.show()
    #开始设置操作
    #开始设置按钮

    sys.exit(app.exec_())  # 最后退出
