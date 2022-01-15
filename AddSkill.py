# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddSkill.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(407, 193)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 351, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.InstructorNameTextEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.InstructorNameTextEdit.setObjectName("InstructorNameTextEdit")
        self.verticalLayout.addWidget(self.InstructorNameTextEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.skillTextEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.skillTextEdit.setObjectName("skillTextEdit")
        self.verticalLayout_2.addWidget(self.skillTextEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.backButton = QtWidgets.QPushButton(self.layoutWidget)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)
        self.addButton = QtWidgets.QPushButton(self.layoutWidget)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 407, 21))
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
        self.label_10.setText(_translate("MainWindow", "Instructor name "))
        self.label_11.setText(_translate("MainWindow", "Skill"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.addButton.setText(_translate("MainWindow", "Add"))


class AddSkill(QtWidgets.QMainWindow):

    def __init__(self, mainMenu, instructor_list):
        super(AddSkill, self).__init__()

        self.mainMenu = mainMenu
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.instructor_list = instructor_list

        self.ui.backButton.clicked.connect(self.back_to_main_menu)
        self.ui.addButton.clicked.connect(self.add_action)

    def back_to_main_menu(self):
        self.hide()
        self.mainMenu.show()

    def add_action(self):
        instructor_name = self.ui.skillTextEdit.toPlainText()
        skill = self.ui.InstructorNameTextEdit.toPlainText()

        for instructor in self.instructor_list:
            if instructor.name == instructor_name:
                instructor.change_name_and_specialisation(instructor_name, skill)
        self.hide()
        self.mainMenu.show()