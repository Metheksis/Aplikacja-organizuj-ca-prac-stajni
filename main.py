# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import QtWidgets, QtCore
from mainwindow import MainWindow
from mainwindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()


    sys.exit(app.exec_())
