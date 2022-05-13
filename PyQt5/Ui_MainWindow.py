# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(60, 120, 89, 25))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(60, 170, 89, 25))
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(60, 220, 89, 25))
        self.pushButton4.setObjectName("pushButton4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(240, 0, 361, 411))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page2 = QtWidgets.QWidget()
        self.page2.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.page2.setObjectName("page2")
        self.start2 = QtWidgets.QPushButton(self.page2)
        self.start2.setGeometry(QtCore.QRect(70, 150, 89, 25))
        self.start2.setObjectName("start2")
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setStyleSheet("background-color: rgb(233, 185, 110);")
        self.page3.setObjectName("page3")
        self.start3 = QtWidgets.QPushButton(self.page3)
        self.start3.setGeometry(QtCore.QRect(130, 170, 89, 25))
        self.start3.setObjectName("start3")
        self.stackedWidget.addWidget(self.page3)
        self.page4 = QtWidgets.QWidget()
        self.page4.setStyleSheet("background-color: rgb(173, 127, 168);")
        self.page4.setObjectName("page4")
        self.start4 = QtWidgets.QPushButton(self.page4)
        self.start4.setGeometry(QtCore.QRect(140, 190, 89, 25))
        self.start4.setObjectName("start4")
        self.stackedWidget.addWidget(self.page4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton2.setText(_translate("MainWindow", "2"))
        self.pushButton3.setText(_translate("MainWindow", "3"))
        self.pushButton4.setText(_translate("MainWindow", "4"))
        self.start2.setText(_translate("MainWindow", "start"))
        self.start3.setText(_translate("MainWindow", "start"))
        self.start4.setText(_translate("MainWindow", "start"))
