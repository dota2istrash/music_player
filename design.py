import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QApplication, QWidget, QMainWindow, QDialog
from PyQt5.QtWidgets import QStatusBar, QMenuBar, QTableWidget, QSlider, QAbstractItemView
from PyQt5.QtWidgets import QDialogButtonBox


class Ui_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"dialog_login")
        self.resize(339, 351)
        self.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.loginButton = QPushButton(self)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(110, 210, 91, 31))
        self.loginButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.createaccButton = QPushButton(self)
        self.createaccButton.setObjectName(u"createaccButton")
        self.createaccButton.setGeometry(QRect(100, 300, 111, 31))
        self.createaccButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.loginLabel = QLabel(self)
        self.loginLabel.setObjectName(u"loginLabel")
        self.loginLabel.setGeometry(QRect(110, 170, 101, 31))
        self.loginLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.createaccLabel = QLabel(self)
        self.createaccLabel.setObjectName(u"createaccLabel")
        self.createaccLabel.setGeometry(QRect(90, 260, 141, 20))
        self.createaccLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.login = QLineEdit(self)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(120, 50, 111, 21))
        self.login.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.password = QLineEdit(self)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(120, 100, 111, 21))
        self.password.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.logLabel = QLabel(self)
        self.logLabel.setObjectName(u"logLabel")
        self.logLabel.setGeometry(QRect(50, 50, 47, 13))
        self.logLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.passwLabel = QLabel(self)
        self.passwLabel.setObjectName(u"passwLabel")
        self.passwLabel.setGeometry(QRect(50, 100, 47, 13))
        self.passwLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.incorrectLabel = QLabel(self)
        self.incorrectLabel.setObjectName(u"incorrectLabel")
        self.incorrectLabel.setGeometry(QRect(100, 140, 150, 21))
        self.incorrectLabel.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle('Вход в учетную запись')
        self.loginButton.setText(QCoreApplication.translate("self", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.createaccButton.setText(QCoreApplication.translate("self",
                                                                u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f",
                                                                None))
        self.loginLabel.setText(QCoreApplication.translate("self",
                                                           u"\u0412\u043e\u0439\u0434\u0438\u0442\u0435 \u0432 \u0430\u043a\u043a\u0430\u0443\u043d\u0442",
                                                           None))
        self.createaccLabel.setText(QCoreApplication.translate("self",
                                                               u"\u041d\u0435\u0442 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430? \u0421\u043e\u0437\u0434\u0430\u0439\u0442\u0435",
                                                               None))
        self.logLabel.setText(QCoreApplication.translate("self", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.passwLabel.setText(QCoreApplication.translate("self", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))


class Ui_Mainwin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"MainWindow")
        self.resize(525, 587)
        self.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.helloLabel = QLabel(self.centralwidget)
        self.helloLabel.setObjectName(u"helloLabel")
        self.helloLabel.setGeometry(QRect(20, 20, 131, 31))
        self.helloLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.playButton = QPushButton(self.centralwidget)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setGeometry(QRect(190, 460, 71, 31))
        self.playButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.loadButton = QPushButton(self.centralwidget)
        self.loadButton.setObjectName(u"loadButton")
        self.loadButton.setGeometry(QRect(270, 20, 81, 31))
        self.loadButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(60, 140, 351, 171))
        self.tableWidget.setStyleSheet((u"color: rgb(54, 54, 54);\n"
                                        "background-color: rgb(255, 255, 255);"))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.volumeChange = QSlider(self.centralwidget)
        self.volumeChange.setObjectName(u"volumeChange")
        self.volumeChange.setGeometry(QRect(390, 500, 121, 16))
        self.volumeChange.setOrientation(Qt.Horizontal)
        self.volumeLabel = QLabel(self.centralwidget)
        self.volumeLabel.setObjectName(u"volumeLabel")
        self.volumeLabel.setGeometry(QRect(370, 500, 16, 21))
        self.volumeLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pauseButton = QPushButton(self.centralwidget)
        self.pauseButton.setObjectName(u"pauseButton")
        self.pauseButton.setGeometry(QRect(190, 500, 75, 23))
        self.pauseButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.prevButton = QPushButton(self.centralwidget)
        self.prevButton.setObjectName(u"prevButton")
        self.prevButton.setGeometry(QRect(100, 500, 75, 23))
        self.prevButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.nextButton = QPushButton(self.centralwidget)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(280, 500, 75, 23))
        self.nextButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(250, 370, 250, 21))
        self.nameLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 370, 91, 21))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 525, 21))
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
        # setupUi

    def retranslateUi(self):
        self.setWindowTitle('Самый лучший музыкальный плеер')
        self.helloLabel.setText("")
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"\u25b6\ufe0f", None))
        self.loadButton.setText(
            QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.volumeLabel.setText('🔊')
        self.pauseButton.setText(QCoreApplication.translate("MainWindow", u"||", None))
        self.prevButton.setText(QCoreApplication.translate("MainWindow", u"|<", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u">|", None))
        self.nameLabel.setText('пока что ничего не играет :(')
        self.label.setText('Сейчас играет:')
        QMetaObject.connectSlotsByName(self)


class OpenFileDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Dialog")
        self.resize(400, 300)
        self.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.accButton = QPushButton(self)
        self.accButton.setObjectName(u"accButton")
        self.accButton.setGeometry(QRect(90, 190, 75, 23))
        self.accButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.rejButton = QPushButton(self)
        self.rejButton.setObjectName(u"rejButton")
        self.rejButton.setGeometry(QRect(220, 190, 75, 23))
        self.rejButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 80, 211, 21))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle('Выберите какой-нибудь трек')
        self.accButton.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430", None))
        self.rejButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u0442", None))
        self.label.setText(QCoreApplication.translate("Dialog",
                                                      u"\u0412\u044b \u0445\u043e\u0442\u0438\u0442\u0435 \u043e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b \u0441 \u043a\u043e\u043c\u043f\u044c\u0442\u0435\u0440\u0430?",
                                                      None))
    # retranslateUi


class Genre_dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Dialog")
        self.resize(398, 132)
        self.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 20, 131, 21))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 60, 161, 21))
        self.lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 100, 75, 23))
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle("Укажите жанр трека")
        self.label.setText(QCoreApplication.translate("Dialog",
                                                      u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0436\u0430\u043d\u0440 \u0442\u0440\u0435\u043a\u0430",
                                                      None))
        self.pushButton.setText('Ok')
    # retranslateUi


class Dialog_urlfile(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Dialog")
        self.resize(400, 300)
        self.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 50, 201, 20))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.fileUrl = QLineEdit(self)
        self.fileUrl.setObjectName(u"fileUrl")
        self.fileUrl.setGeometry(QRect(102, 130, 201, 20))
        self.fileUrl.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(180, 220, 91, 21))
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle('Ввод ссылки на трек')
        self.label.setText(QCoreApplication.translate("Dialog",
                                                      u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0441\u044b\u043b\u043a\u0443 \u043d\u0430 \u043c\u0443\u0437\u044b\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0444\u0430\u0439\u043b",
                                                      None))
        self.fileUrl.setText("")
        self.pushButton.setText('Ok')
    # retranslateUi
