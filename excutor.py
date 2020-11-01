# -*- coding: utf-8 -*-
# Sci自动下载
import requests
import lxml.etree
import re
from tkinter import filedialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget       #一个是程序，一个是窗口
import sys
from design import scidownload_gui

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
    myui.pushButton.clicked.connect(start_download)
    myui.pushButton_2.clicked.connect(import_pmid_list)
    myui.pushButton_3.clicked.connect(change_dir)
    sys.exit(app.exec_())  # 最后退出



