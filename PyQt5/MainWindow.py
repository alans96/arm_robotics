#
# Funções 
#

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_MainWindow import Ui_MainWindow
###########################################
import cv2
import numpy as np
import PoseModule as pm
from openpyxl import Workbook
###########################################

class MainWindow():
    def __init__(self, ):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Define qual tela inicia
        self.ui.Pages.setCurrentWidget(self.ui.page_home)

        # Botão do menu
        self.ui.btn_contatos.clicked.connect(self.show_contatos)
        self.ui.btn_funcoes.clicked.connect(self.show_funcao)
        self.ui.btn_home.clicked.connect(self.show_home)
        self.ui.btn_sobre.clicked.connect(self.show_sobre)

        # Botão Start
        self.ui.start.clicked.connect(self.show_btn)


        #ComboBox (Selecionar a quant. de classe)
        

        # Variância  

        # N. Amostra



    def show(self):
        self.main_win.show()


    ##############################
    # Função do botão menu
    ##############################
    def show_contatos(self):
        self.ui.Pages.setCurrentWidget(self.ui.page_contatos) 
    def show_home(self):
        self.ui.Pages.setCurrentWidget(self.ui.page_home)
    def show_funcao(self):
        self.ui.Pages.setCurrentWidget(self.ui.page_funcoes)
    def show_sobre(self):
        self.ui.Pages.setCurrentWidget(self.ui.page_sobre)
    

    #######################################
    # Função do botão Start
    #######################################
    def show_btn(self):
        
        # Escolher a quantidade de classes
        teste = int(self.ui.comboBox.currentText())

        # variação do ângulo
        var = int(self.ui.lineEdit_var.text())

        # Numero de amostragem
        #num = int(self.ui.lineEdit_amostra.text())


    
        ###############################
        #        CODIGO DUMMY
        ###############################
        
        cap = cv2.VideoCapture(0)  # Fonte da imagem
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # Fonte da imagem
        out = cv2.VideoWriter('test_r.avi', fourcc, 20.0, (640, 480))  # Formato do vídeo
        
                #  Criação do excel
        wb = Workbook()
        #  workbook_name = "Left_Arm.xlsx"
        workbook_name = "Right_Arm.xlsx"
        wb1 = wb.active
        wb1.title = "Landmarks"
        wb1.append(["LandmarkX 12", "LandmarkY 12", "LandmarkX 14", "LandmarkY 14",
                    "LandmarkX 16", "LandmarkY 16", "Angle"])

        detector = pm.PoseDetector()
        count = 0
        dir = 0

        while cap.isOpened():
            # Captura e espelhamento do vídeo
            ret, img = cap.read()
            img = cv2.flip(img, 180)

            if ret is True:
                #  Detectar o corpo e marcadores sem desenhar
                img = detector.findPose(img, False)
                lmList = detector.findPosition(img, False)

                # Lista de marcadores
                if len(lmList) != 0:
                    try:
                        # Right Arm
                        angle = detector.findAngle(img, 11, 13, 15)
                        # fazer o angulo converter de 0 a 100
                        per = np.interp(angle, (40, 171), (0, 100))
                        # barra
                        bar = np.interp(angle, (40, 171), (400, 100))
                        # print(int(angle), int(per))

                        # Contagem das repetições
                        if per == 0:
                            if dir == 0:
                                count += 0.5
                                dir = 1
                        if per == 100:
                            if dir == 1:
                                count += 0.5
                                dir = 0

                    finally:
                        # Barra retangular fixa
                        cv2.rectangle(img, (50, 400), (50, 400), (0, 255, 0), 3)
                        # Barra móvel
                        cv2.rectangle(img, (50, int(bar)), (60, 400), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, f'{int(per)}%', (55, 300), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 4)

                        # Número da repetição
                        cv2.putText(img, str(int(count)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
                        
                        # Teste 1
                        if teste == 1:
                            if 90 - var < angle < 91 + var:
                                wb1.append([lmList[11][1], lmList[11][2], lmList[13][1], lmList[13][2],
                                            lmList[15][1], lmList[15][2], 1])
                            elif 180 - var < angle < 180:
                                wb1.append([lmList[11][1], lmList[11][2], lmList[13][1], lmList[13][2],
                                            lmList[15][1], lmList[15][2], 0])

                        # Teste 2
                        if teste == 2:
                            if 90 - var < angle < 91 + var:
                                wb1.append([lmList[11][1], lmList[11][2], lmList[13][1], lmList[13][2],
                                            lmList[15][1], lmList[15][2], 2])

                            elif 180 - var < angle < 180:
                                wb1.append([lmList[11][1], lmList[11][2], lmList[13][1], lmList[13][2],
                                            lmList[15][1], lmList[15][2], 0])

                            elif 30 - var < angle < 31 + var:
                                wb1.append([lmList[11][1], lmList[11][2], lmList[13][1], lmList[13][2],
                                            lmList[15][1], lmList[15][2], 1])

                        # Teste 3
                        if teste == 3:
                            if 180 - var < angle < 180:
                                wb1.append([lmList[11][1], lmList[11][2], lmList[13][1], lmList[13][2],
                                            lmList[15][1], lmList[15][2], 0])

                            elif 30 - var < angle < 31 + var:
                                wb1.append([lmList[11][1], lmList[11][2], lmList[13][1], lmList[13][2],
                                            lmList[15][1], lmList[15][2], 1])
                            elif 45 - var < angle < 41 + var:
                                wb1.append([lmList[11][1], lmList[11][2], lmList[13][1], lmList[13][2],
                                            lmList[15][1], lmList[15][2], 2])

                            elif 90 - var < angle < 91 + var:
                                wb1.append([lmList[11][1], lmList[11][2], lmList[13][1], lmList[13][2],
                                            lmList[15][1], lmList[15][2], 3])

                    """try:
                        # Left Arm
                        angle = detector.findAngle(img, 12, 14, 16)
                        per = np.interp(angle, (217, 315), (0, 100))
                        bar = np.interp(angle, (217, 315), (400, 100))
                        lmList = detector.findPosition(img, draw=False)
                        print(lmList[12])
                        if per == 0:
                            if dir == 0:
                                count += 0.5
                                dir = 1
                        if per == 100:
                            if dir == 1:
                                count += 0.5
                                dir = 0
                    finally:
                        # barra retangular
                        cv2.rectangle(img, (50, 400), (50, 400), (0, 255, 0), 3)
                        cv2.rectangle(img, (50, int(bar)), (60, 400), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, f'{int(per)}%', (55, 300), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 4)
                        # repetição
                        cv2.putText(img, str(int(count)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

                        # Excel
                        wb1.append([lmList[12][1], lmList[12][2], lmList[14][1], lmList[14][2],
                                    lmList[16][1], lmList[16][2], angle])"""

                out.write(img)
                cv2.imshow("Image", img)

                if cv2.waitKey(10) == ord('q'):
                    break

            else:
                print("Webcam não encontrada")
                break

        # Finalizar os arquivos
        wb.save(filename=workbook_name)
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        ###############################
        #        CODIGO DUMMY
        ###############################'''
    

# Inicializar
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win= MainWindow()
    main_win.show()
    sys.exit(app.exec())
