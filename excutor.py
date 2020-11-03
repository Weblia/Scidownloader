# -*- coding: utf-8 -*-
# Sci自动下载
import requests
import lxml.etree
import re
from tkinter import filedialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QWidget  # 一个是程序，一个是窗口
import sys
from scidownload_gui import Ui_MainWindow
from sci_hub_driver_functions import download_pmid, validatetitle
from PyQt5.QtCore import QThread, pyqtSignal, QMutex


q_mute = QMutex()


class DownloadThread(QThread):  # 建立一个任务线程类
    signal = pyqtSignal(str)  # 设置触发信号传递的参数数据类型,这里是字符串
    # data ={}
    # the_paper_id = ''
    # file_dir = ''

    def __init__(self):
        super(DownloadThread, self).__init__()

    def run(self):  # 在启动线程后任务从这个函数里面开始执行
        print('开始锁定')
        q_mute.lock()
        print('开始上网请求')
        download_pmid(self.data, self.the_paper_id, self.file_dir)
        print('开始解锁')
        q_mute.unlock()


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        # 将UI应用于生成的主窗口
        self.setupUi(self)
        self.download_thread = DownloadThread()
        # 构造时就设置按钮链接
        self.pushButton.clicked.connect(self.start_download)
        self.pushButton_2.clicked.connect(self.import_pmid_list)
        self.pushButton_3.clicked.connect(self.change_dir)
        self.textEdit.setText('25412137\n22634648\n26943142\n27926456')
        self.plainTextEdit.setPlainText('C:/Users/Administrator/Desktop/test文献')
    def start_download(self):
        pmid_text = self.textEdit.toPlainText()
        pmid_list = pmid_text.rstrip().split('\n')
        print(pmid_list)
        lines = pmid_text.count('\n') + 1
        print('共' + str(lines) + '篇文献')
        # 开始装载request请求
        data = {  # 先完善表单内容
            'request': 'undefined'
        }
        for i in pmid_list:
            data['request'] = i
            the_paper_id = i
            print('开始下载： ' + the_paper_id)
            # 先把参数传递进线程
            # 实例化自己建立的任务线程类
            self.download_thread.start()  # 然后开始run()方法，run()方法的参数用传进去的参数进行
            print('开始设置1')
            self.download_thread.data = data
            print('开始设置2')
            self.download_thread.the_paper_id = the_paper_id
            self.download_thread.file_dir = self.plainTextEdit.toPlainText()

    def import_pmid_list(self):
        fname = QFileDialog.getOpenFileName(self)
        with open(fname[0], 'r') as f:
            data = f.read()
            self.textEdit.setText(data)

    def change_dir(self):
        f_dir = QFileDialog.getExistingDirectory(self)
        self.plainTextEdit.setPlainText(f_dir)


if __name__ == "__main__":
    # 创建一个app实例
    app = QApplication(sys.argv)
    # 建立一个主窗口
    mymainwindow = MyMainWindow()
    mymainwindow.show()
    # 开始设置操作
    # 开始设置按钮

    sys.exit(app.exec_())  # 最后退出
