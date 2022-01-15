from PyQt5 import QtCore, QtGui, QtWidgets
from AddHorseToCare import AddHorseToCareWindow
from CreateGroomWindow import CreateGroomWindow
from CreateStableWindow import CreateStableWindow
from CreateInstructorWindow import CreateInstructorWindow
from AddHorseWindow import AddHorseWindow
from BookRide import BookRideWindow
from AddSkill import AddSkill
import Functionalities as fn

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(482, 488)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 20, 431, 411))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.createStableButton = QtWidgets.QPushButton(self.widget)
        self.createStableButton.setObjectName("createStableButton")
        self.verticalLayout.addWidget(self.createStableButton)
        self.addHorseButtorn = QtWidgets.QPushButton(self.widget)
        self.addHorseButtorn.setObjectName("addHorseButtorn")
        self.verticalLayout.addWidget(self.addHorseButtorn)
        self.createGroomButton = QtWidgets.QPushButton(self.widget)
        self.createGroomButton.setObjectName("createGroomButton")
        self.verticalLayout.addWidget(self.createGroomButton)
        self.createInstructorButton = QtWidgets.QPushButton(self.widget)
        self.createInstructorButton.setObjectName("createInstructorButton")
        self.verticalLayout.addWidget(self.createInstructorButton)
        self.addHorseCareButton = QtWidgets.QPushButton(self.widget)
        self.addHorseCareButton.setObjectName("addHorseCareButton")
        self.verticalLayout.addWidget(self.addHorseCareButton)
        self.bookRideButton = QtWidgets.QPushButton(self.widget)
        self.bookRideButton.setObjectName("bookRideButton")
        self.verticalLayout.addWidget(self.bookRideButton)
        self.generatePlanButton = QtWidgets.QPushButton(self.widget)
        self.generatePlanButton.setObjectName("generatePlanButton")
        self.verticalLayout.addWidget(self.generatePlanButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 482, 21))
        self.menubar.setObjectName("menubar")
        self.menuStable_appl = QtWidgets.QMenu(self.menubar)
        self.menuStable_appl.setObjectName("menuStable_appl")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuStable_appl.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.createGroomButton.setText(_translate("MainWindow", "Create Groom"))
        self.createStableButton.setText(_translate("MainWindow", "Create Stable"))
        self.createInstructorButton.setText(_translate("MainWindow", "Create Instructor"))
        self.addHorseButtorn.setText(_translate("MainWindow", "Add Horse"))
        self.addHorseCareButton.setText(_translate("MainWindow", "Add horse care"))
        self.bookRideButton.setText(_translate("MainWindow", "Book ride"))
        self.generatePlanButton.setText(_translate("MainWindow", "Generate plan"))
        self.menuStable_appl.setTitle(_translate("MainWindow", "Stable appl"))


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        #bind all buttons to coresponding action
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.addHorseCareButton.clicked.connect(self.got_to_add_horse_care)
        self.ui.createGroomButton.clicked.connect(self.got_to_create_groom)
        self.ui.createStableButton.clicked.connect(self.got_to_create_stable)
        self.ui.createInstructorButton.clicked.connect(self.got_to_create_instructor)
        self.ui.addHorseButtorn.clicked.connect(self.got_to_add_horse)
        self.ui.bookRideButton.clicked.connect(self.got_to_book_ride)
        self.ui.generatePlanButton.clicked.connect(self.generate_plan)

        self.owner = fn.Stable_owner("")
        self.stable = fn.Stable("")
        self.groom_list = []
        self.instructor_list = []

    def got_to_add_horse_care(self):
        self.hide()
        self.addHorseToCareWindow = AddHorseToCareWindow(self, self.groom_list, self.stable)
        self.addHorseToCareWindow.show()

    def got_to_add_horse(self):
        self.hide()
        self.addHorse = AddHorseWindow(self, self.stable)
        self.addHorse.show()

    def got_to_create_groom(self):
        self.hide()
        self.create_groom = CreateGroomWindow(self, self.groom_list)
        self.create_groom.show()

    def got_to_create_stable(self):
        self.hide()
        self.create_stable = CreateStableWindow(self, self.stable)
        self.create_stable.show()

    def got_to_create_instructor(self):
        self.hide()
        self.create_instructor = CreateInstructorWindow(self, self.instructor_list)
        self.create_instructor.show()

    def got_to_book_ride(self):
        self.hide()
        self.book_ride = BookRideWindow(self, self.instructor_list, self.stable)
        self.book_ride.show()

    def generate_plan(self):
        self.stable.generate_plan(self.groom_list, self.instructor_list)
        for groom in self.groom_list:
            groom.generate_plan(self.stable)
        for instructor in self.instructor_list:
            instructor.generate_plan()