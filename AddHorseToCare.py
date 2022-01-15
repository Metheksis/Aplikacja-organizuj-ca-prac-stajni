from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 162)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 120, 351, 21))
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
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 351, 96))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.groomName = QtWidgets.QTextEdit(self.widget)
        self.groomName.setObjectName("groomName")
        self.verticalLayout.addWidget(self.groomName)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horseName = QtWidgets.QTextEdit(self.widget)
        self.horseName.setObjectName("horseName")
        self.verticalLayout_2.addWidget(self.horseName)
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
        self.label_3.setText(_translate("MainWindow", "Groom`s Name "))
        self.label_4.setText(_translate("MainWindow", "Horse name"))


class AddHorseToCareWindow(QtWidgets.QMainWindow):

    def __init__(self, mainMenu, grooms_list, stable):
        super(AddHorseToCareWindow, self).__init__()

        self.mainMenu = mainMenu
        self.grooms_list = grooms_list
        self.stable = stable
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.backButton.clicked.connect(self.back_to_main_menu)
        self.ui.addButton.clicked.connect(self.add_to_list)

    def back_to_main_menu(self):
        self.hide()
        self.mainMenu.show()

    def add_to_list(self):
        grooms_name = self.ui.groomName.toPlainText()
        horse_name = self.ui.horseName.toPlainText()

        for groom in self.grooms_list:
            if groom.name == grooms_name:
                horse = self.stable.get_horse_by_name(horse_name)
                groom.add_horse_to_care(horse)

        self.hide()
        self.mainMenu.show()
