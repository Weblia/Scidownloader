# -*- coding: utf-8 -*-
# pyQt5 界面

from PyQt5.QtWidgets import QApplication, QWidget       #一个是程序，一个是窗口
import sys

if __name__ == "__main__":
    # 创建一个app实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置窗口尺寸
    w.resize(600,300)
    # 移动窗口
    w.move(650,350)
    w.setWindowTitle('Sci批量下载工具')
    #显示窗口
    w.show()
    # 进入程序主循环，并通过exit安全结束
    sys.exit(app.exec_())
