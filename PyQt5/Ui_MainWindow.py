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
        MainWindow.setStyleSheet("*{\n"
"border:none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_container = QtWidgets.QFrame(self.centralwidget)
        self.left_container.setMaximumSize(QtCore.QSize(150, 16777215))
        self.left_container.setStyleSheet("")
        self.left_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_container.setObjectName("left_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_container)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.left_container)
        self.frame_2.setStyleSheet("QToolBox::tab{\n"
"    border-radius: 5px;\n"
"\n"
"    \n"
"    background-color: rgb(211, 215, 207);\n"
"}\n"
"\n"
"QFrame{\n"
"    \n"
"    background-color: rgb(136, 138, 133);\n"
"    border-radius: 5px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.toolbox = QtWidgets.QToolBox(self.frame_2)
        self.toolbox.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.toolbox.setObjectName("toolbox")
        self.Menu = QtWidgets.QWidget()
        self.Menu.setGeometry(QtCore.QRect(0, 0, 132, 315))
        self.Menu.setObjectName("Menu")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Menu)
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_home = QtWidgets.QPushButton(self.Menu)
        self.btn_home.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_home.setStyleSheet("QPushButton:hover{\n"
"    border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"    border-bottom-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    \n"
"    background-color: rgb(211, 215, 207);\n"
"}\n"
"\n"
"")
        self.btn_home.setAutoDefault(False)
        self.btn_home.setObjectName("btn_home")
        self.verticalLayout_4.addWidget(self.btn_home)
        self.btn_funcoes = QtWidgets.QPushButton(self.Menu)
        self.btn_funcoes.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_funcoes.setStyleSheet("QPushButton:hover{\n"
"    border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"    border-bottom-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    \n"
"    background-color: rgb(211, 215, 207);\n"
"}")
        self.btn_funcoes.setObjectName("btn_funcoes")
        self.verticalLayout_4.addWidget(self.btn_funcoes)
        self.btn_contatos = QtWidgets.QPushButton(self.Menu)
        self.btn_contatos.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_contatos.setStyleSheet("QPushButton:hover{\n"
"    border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"    border-bottom-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    \n"
"    background-color: rgb(211, 215, 207);\n"
"}\n"
"")
        self.btn_contatos.setObjectName("btn_contatos")
        self.verticalLayout_4.addWidget(self.btn_contatos)
        self.btn_sobre = QtWidgets.QPushButton(self.Menu)
        self.btn_sobre.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_sobre.setStyleSheet("QPushButton:hover{\n"
"    border-top-left-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"    border-bottom-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"    \n"
"    background-color: rgb(211, 215, 207);\n"
"}")
        self.btn_sobre.setObjectName("btn_sobre")
        self.verticalLayout_4.addWidget(self.btn_sobre)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.toolbox.addItem(self.Menu, "")
        self.verticalLayout_3.addWidget(self.toolbox)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.left_container)
        self.main_container = QtWidgets.QFrame(self.centralwidget)
        self.main_container.setStyleSheet("QFrame{\n"
"    \n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.main_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_container.setObjectName("main_container")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_container)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QtWidgets.QFrame(self.main_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top.sizePolicy().hasHeightForWidth())
        self.top.setSizePolicy(sizePolicy)
        self.top.setMinimumSize(QtCore.QSize(0, 30))
        self.top.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(136, 138, 133);\n"
"    border-radius: 5px;\n"
"}")
        self.top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top.setObjectName("top")
        self.label = QtWidgets.QLabel(self.top)
        self.label.setGeometry(QtCore.QRect(50, 10, 331, 16))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.top)
        self.main_center = QtWidgets.QFrame(self.main_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_center.sizePolicy().hasHeightForWidth())
        self.main_center.setSizePolicy(sizePolicy)
        self.main_center.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(136, 138, 133);\n"
"    border-radius: 5px;\n"
"}")
        self.main_center.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_center.setObjectName("main_center")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.main_center)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Pages = QtWidgets.QStackedWidget(self.main_center)
        self.Pages.setObjectName("Pages")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_home)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.logo = QtWidgets.QLabel(self.page_home)
        self.logo.setObjectName("logo")
        self.verticalLayout_7.addWidget(self.logo)
        self.label_3 = QtWidgets.QLabel(self.page_home)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.Pages.addWidget(self.page_home)
        self.page_funcoes = QtWidgets.QWidget()
        self.page_funcoes.setObjectName("page_funcoes")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_funcoes)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.page_funcoes)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.frame_main = QtWidgets.QFrame(self.page_funcoes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_main.sizePolicy().hasHeightForWidth())
        self.frame_main.setSizePolicy(sizePolicy)
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.frame_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4)
        self.lineEdit_amostra = QtWidgets.QLineEdit(self.frame_main)
        self.lineEdit_amostra.setStyleSheet("font: \'Quantidade de Amostra\'11pt \"Ubuntu\";\n"
"color: rgb(0, 0, 0);\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"    \n"
"background-color: rgb(211, 215, 207);")
        self.lineEdit_amostra.setText("")
        self.lineEdit_amostra.setObjectName("lineEdit_amostra")
        self.verticalLayout_9.addWidget(self.lineEdit_amostra)
        self.label_5 = QtWidgets.QLabel(self.frame_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.lineEdit_var = QtWidgets.QLineEdit(self.frame_main)
        self.lineEdit_var.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"    \n"
"background-color: rgb(211, 215, 207);")
        self.lineEdit_var.setText("")
        self.lineEdit_var.setObjectName("lineEdit_var")
        self.verticalLayout_9.addWidget(self.lineEdit_var)
        self.comboBox = QtWidgets.QComboBox(self.frame_main)
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"    \n"
"background-color: rgb(211, 215, 207);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_9.addWidget(self.comboBox)
        self.start = QtWidgets.QPushButton(self.frame_main)
        self.start.setStyleSheet("border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"    \n"
"background-color: rgb(211, 215, 207);\n"
"\n"
"")
        self.start.setObjectName("start")
        self.verticalLayout_9.addWidget(self.start)
        self.verticalLayout_8.addWidget(self.frame_main)
        self.Pages.addWidget(self.page_funcoes)
        self.page_contatos = QtWidgets.QWidget()
        self.page_contatos.setObjectName("page_contatos")
        self.label_12 = QtWidgets.QLabel(self.page_contatos)
        self.label_12.setGeometry(QtCore.QRect(20, 10, 31, 31))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page_contatos)
        self.label_13.setGeometry(QtCore.QRect(20, 40, 67, 17))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page_contatos)
        self.label_14.setGeometry(QtCore.QRect(20, 70, 67, 17))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page_contatos)
        self.label_15.setGeometry(QtCore.QRect(20, 90, 67, 17))
        self.label_15.setObjectName("label_15")
        self.Pages.addWidget(self.page_contatos)
        self.page_sobre = QtWidgets.QWidget()
        self.page_sobre.setObjectName("page_sobre")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_sobre)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_16 = QtWidgets.QLabel(self.page_sobre)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.page_sobre)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_6.addWidget(self.label_17)
        self.Pages.addWidget(self.page_sobre)
        self.verticalLayout_5.addWidget(self.Pages)
        self.verticalLayout.addWidget(self.main_center)
        self.baseboard = QtWidgets.QFrame(self.main_container)
        self.baseboard.setMinimumSize(QtCore.QSize(0, 35))
        self.baseboard.setStyleSheet("QFrame{\n"
"\n"
"    background-color: rgb(136, 138, 133);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.baseboard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.baseboard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.baseboard.setObjectName("baseboard")
        self.base = QtWidgets.QLabel(self.baseboard)
        self.base.setGeometry(QtCore.QRect(0, 0, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.base.setFont(font)
        self.base.setObjectName("base")
        self.verticalLayout.addWidget(self.baseboard)
        self.horizontalLayout.addWidget(self.main_container)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolbox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_home.setText(_translate("MainWindow", "Home"))
        self.btn_funcoes.setText(_translate("MainWindow", "Funções"))
        self.btn_contatos.setText(_translate("MainWindow", "Contatos"))
        self.btn_sobre.setText(_translate("MainWindow", "Sobre"))
        self.toolbox.setItemText(self.toolbox.indexOf(self.Menu), _translate("MainWindow", "Page 1"))
        self.label.setText(_translate("MainWindow", "Sistema de Captura de Posições do Braço"))
        self.logo.setText(_translate("MainWindow", "imagem da uf"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Projeto de Iniciação Cientifica</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Parâmetros"))
        self.label_4.setText(_translate("MainWindow", "Quantidade de Amostra"))
        self.label_5.setText(_translate("MainWindow", "Variância"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Selecione a Quantidade de Classe"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.label_12.setText(_translate("MainWindow", "Git"))
        self.label_13.setText(_translate("MainWindow", "link: "))
        self.label_14.setText(_translate("MainWindow", "Email"))
        self.label_15.setText(_translate("MainWindow", "...."))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Sobre</p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "Texto sobre o programa"))
        self.base.setText(_translate("MainWindow", "PyArmy"))
