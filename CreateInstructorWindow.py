# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateInstructorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Functionalities as fn

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(395, 193)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 130, 351, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.backButton = QtWidgets.QPushButton(self.layoutWidget)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)
        self.addButton = QtWidgets.QPushButton(self.layoutWidget)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 30, 351, 96))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.instructorName = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.instructorName.setObjectName("instructorName")
        self.verticalLayout.addWidget(self.instructorName)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.specialisationName = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.specialisationName.setObjectName("specialisationName")
        self.verticalLayout_2.addWidget(self.specialisationName)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.label_3.setText(_translate("MainWindow", "Instructor`s Name "))
        self.label_4.setText(_translate("MainWindow", "Specialisation"))


class CreateInstructorWindow(QtWidgets.QMainWindow):

    def __init__(self, mainMenu, instructor_list):
        super(CreateInstructorWindow, self).__init__()

        self.mainMenu = mainMenu
        self.instructor_list = instructor_list
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.backButton.clicked.connect(self.back_to_main_menu)
        self.ui.addButton.clicked.connect(self.add_instructor)

    def back_to_main_menu(self):
        self.hide()
        self.mainMenu.show()

    def add_instructor(self):
        name = self.ui.instructorName.toPlainText()
        special = self.ui.specialisationName.toPlainText()
        self.instructor_list.append(fn.RidingInstructor(name, special))
        self.hide()
        self.mainMenu.show()