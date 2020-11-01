# -*- coding: utf-8 -*-
# Sci自动下载

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget       #一个是程序，一个是窗口
import sys
from design import scidownload_gui
from design import linker




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
    sys.exit(app.exec_())


