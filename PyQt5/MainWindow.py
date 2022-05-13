#
# Funções 
#


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog 
from PyQt5 import uic
from Ui_MainWindow import Ui_MainWindow


class MainWindow():
    def __init__(self, ):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Define qual tela inicia
        self.ui.stackedWidget.setCurrentWidget(self.ui.page2)

        self.ui.pushButton2.clicked.connect(self.show2)
        self.ui.pushButton3.clicked.connect(self.show3)
        self.ui.pushButton4.clicked.connect(self.show4)
        self.ui.start2.clicked.connect(self.openpy)

    def show(self):
        self.main_win.show()
    
    # Função do botão
    def show2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page2)
    
    def show3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page3)
    
    def show4(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page4)

    def openpy(self):
        caminho,_ = QFileDialog.getOpenFileName(None, 'Abrir um Arquivo Python', "/home/alan/Projetos", 'Arquivo Python(*.py)')
        
        
    

    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win= MainWindow()
    main_win.show()
    sys.exit(app.exec())