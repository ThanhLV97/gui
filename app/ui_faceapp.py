# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/thanhlv/workspace/projects/gui/Splash_Screen_Python_PySide2/ui_app/faceappv1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 400)
        MainWindow.setMaximumSize(QtCore.QSize(680, 400))
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        font = QtGui.QFont()
        font.setKerning(True)
        self.centralwidget.setFont(font)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setEnabled(True)
        self.background.setStyleSheet("QFrame {    \n"
"    background-color: rgb(22, 105, 122);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.adduser = QtWidgets.QPushButton(self.background)
        self.adduser.setGeometry(QtCore.QRect(70, 250, 89, 25))
        self.adduser.setStyleSheet("QPushButton  {    \n"
"    background-color: rgb(240, 84, 84);\n"
"    color: rgb(220,220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.adduser.setObjectName("adduser")
        self.checkin = QtWidgets.QPushButton(self.background)
        self.checkin.setGeometry(QtCore.QRect(70, 130, 89, 25))
        self.checkin.setAutoFillBackground(False)
        self.checkin.setStyleSheet("QPushButton  {    \n"
"    background-color: rgb(240, 84, 84);\n"
"    color: rgb(220,220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.checkin.setObjectName("checkin")
        self.label = QtWidgets.QLabel(self.background)
        self.label.setGeometry(QtCore.QRect(30, 20, 131, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".../image/dsoftv2.jpg.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.background)
        self.dateTimeEdit.setGeometry(QtCore.QRect(380, 20, 194, 31))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_2 = QtWidgets.QLabel(self.background)
        self.label_2.setGeometry(QtCore.QRect(220, 90, 401, 251))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(".../image/faceappiconv2.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.background)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.adduser.setText(_translate("MainWindow", "Add a user"))
        self.checkin.setText(_translate("MainWindow", "Checkin"))

