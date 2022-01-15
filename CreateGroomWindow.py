# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateGroomWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Functionalities as fn

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(285, 192)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 241, 128))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.groomNameTextEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.groomNameTextEdit.setObjectName("groomNameTextEdit")
        self.verticalLayout_8.addWidget(self.groomNameTextEdit)
        self.verticalLayout.addLayout(self.verticalLayout_8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.backButton = QtWidgets.QPushButton(self.layoutWidget)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)
        self.addButton = QtWidgets.QPushButton(self.layoutWidget)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 285, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "Groom`s name "))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.addButton.setText(_translate("MainWindow", "Add"))

class CreateGroomWindow(QtWidgets.QMainWindow):

    def __init__(self, mainMenu, grooms_list):
        super(CreateGroomWindow, self).__init__()

        self.mainMenu = mainMenu
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.grooms_list = grooms_list
        self.ui.backButton.clicked.connect(self.back_to_main_menu)
        self.ui.addButton.clicked.connect(self.add_to_list)

    def back_to_main_menu(self):
        self.hide()
        self.mainMenu.show()

    def add_to_list(self):
        name = self.ui.groomNameTextEdit.toPlainText()
        self.grooms_list.append(fn.Groom(name))
        self.hide()
        self.mainMenu.show()