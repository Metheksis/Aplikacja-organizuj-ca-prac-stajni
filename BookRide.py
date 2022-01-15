# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BookRide.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Functionalities as fn

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 456)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 10, 501, 207))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.InstructorNameTextEdit = QtWidgets.QTextEdit(self.widget)
        self.InstructorNameTextEdit.setObjectName("InstructorNameTextEdit")
        self.verticalLayout.addWidget(self.InstructorNameTextEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.horseTextEdit = QtWidgets.QTextEdit(self.widget)
        self.horseTextEdit.setObjectName("horseTextEdit")
        self.verticalLayout_2.addWidget(self.horseTextEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.RiderTextEdit = QtWidgets.QTextEdit(self.widget)
        self.RiderTextEdit.setObjectName("RiderTextEdit")
        self.verticalLayout_3.addWidget(self.RiderTextEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.timeEdit = QtWidgets.QTimeEdit(self.widget)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout_4.addWidget(self.timeEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.backButton = QtWidgets.QPushButton(self.widget)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)
        self.addButton = QtWidgets.QPushButton(self.widget)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.errorLabel = QtWidgets.QLabel(self.widget)
        self.errorLabel.setObjectName("errorLabel")
        self.verticalLayout_5.addWidget(self.errorLabel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "Instructor name "))
        self.label_11.setText(_translate("MainWindow", "Horse name"))
        self.label_12.setText(_translate("MainWindow", "Rider name"))
        self.label_13.setText(_translate("MainWindow", "Ride hour"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.errorLabel.setText(_translate("MainWindow", ""))


class BookRideWindow(QtWidgets.QMainWindow):

    def __init__(self, mainMenu, instructor_list, stable):
        super(BookRideWindow, self).__init__()

        self.mainMenu = mainMenu
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.instructor_list = instructor_list
        self.stable = stable

        self.ui.backButton.clicked.connect(self.back_to_main_menu)
        self.ui.addButton.clicked.connect(self.add_action)

    def back_to_main_menu(self):
        self.hide()
        self.mainMenu.show()

    def add_action(self):
        riderName = self.ui.RiderTextEdit.toPlainText()
        horseName = self.ui.horseTextEdit.toPlainText()
        instructorName = self.ui.InstructorNameTextEdit.toPlainText()
        startH = self.ui.timeEdit.text()

        for instructor in self.instructor_list:
            if instructor.name == instructorName:
                instructor.book_ride(self.stable, horseName, startH, riderName)
                break

        self.hide()
        self.mainMenu.show()
