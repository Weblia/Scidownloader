# -*- coding: utf-8 -*-
# Sci自动下载

s_name = '123153141'
s_path = 'C:\\Users\\x1c\\Desktop\\scidownload\\'+s_name
import requests
import lxml.etree
import re
from tkinter import filedialog

Fpath = filedialog.askopenfilename()
print(Fpath)


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