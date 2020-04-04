#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

    def msg(self):
        files, ok1 = QFileDialog.getOpenFileNames(self,
                                                  "多文件选择",
                                                  "/home/kedong",
                                                  "All Files (*);;Text Files (*.txt)")
        print(files)
        if len(files) > 0:
            filesPath = ''
            for file in files:
                filesPath += (file + ' ')
            cmd = f'adb push {filesPath} /sdcard/tencent/MicroMsg/Download/'
            print(cmd)
            os.popen(cmd)
            


if __name__ == "__main__":
        # 判断是否有手机连接
    result = os.popen('adb devices -l')
    textArr = result.readlines()
    if len(textArr) == 2:
        os._exit(0)

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.msg()
    # myshow.show()
    # sys.exit(app.exec_())
    os._exit(0)
