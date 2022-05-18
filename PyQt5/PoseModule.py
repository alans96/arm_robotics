import cv2
import mediapipe as mp
import math

################
from Ui_MainWindow import Ui_MainWindow
################


class PoseDetector:  # Classe para detectar pessoas

    # Parâmetros do pose
    def __init__(self, static_image_mode=False, model_complexity=1, smooth_landmarks=True,
                 enable_segmentation=False, smooth_segmentation=True, min_detection_confidence=0.5,
                 min_tracking_confidence=0.5):
        # Sempre que criar um novo objeto terá suas próprias variáveis
        self.static_image_mode = static_image_mode
        self.model_complexity = model_complexity
        self.smooth_landmarks = smooth_landmarks
        self.enable_segmentation = enable_segmentation
        self.smooth_segmentation = smooth_segmentation
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.static_image_mode, self.model_complexity, self.smooth_landmarks,
                                     self.enable_segmentation, self.smooth_segmentation, self.min_detection_confidence,
                                     self.min_tracking_confidence)
        
        ##########
        self.ui = Ui_MainWindow()
        self.ui.start.clicked.connect(self.show_btn)
        #########

    ###########    
    def show_btn(self):
        
        # Escolher a quantidade de classes
        teste = int(self.ui.comboBox.currentText())

        # variação do ângulo
        var = int(self.ui.lineEdit_var.text())

        # Numero de amostragem
        #num = int(self.ui.lineEdit_amostra.text())
        return teste, var
   
        ############

    def findPose(self, img, draw=True):
        """Encontra o corpo da pessoa"""
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return img

    def findPosition(self, img, draw=True):
        """Encontra os valores de x e y de cada ponto(landmark) e colocar em uma lista"""
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # Calcula o valor do pixel de cada ponto
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 3, (255, 0, 0), cv2.FILLED)
        return self.lmList

    def findAngle(self, img, p1, p2, p3, draw=True):
        """Encontra o ângulo entre 2 pontos"""
        # Adicionar os valores de x e y dos marcadores nas variáveis
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

        # Cálculo do ângulo
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                             math.atan2(y1 - y2, x1 - x2))

        # Não mostrar ângulo negativo
        if angle < 0:
            angle += 360

        if draw:
# Qual teste será usado

            # Teste 1
            if self.teste == 1:
                if 90-self.var < angle < 91+self.var or 180-self.var < angle < 180:
                    # Desenhar linha de conecção entre os pontos
                    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.line(img, (x3, y3), (x2, y2), (0, 0, 255), 3)

                    # Desenhar 2 circulos entre os marcadores de interesse
                    cv2.circle(img, (x1, y1), 4, (50, 200, 255), cv2.FILLED)
                    cv2.circle(img, (x1, y1), 8, (50, 200, 255), 2)
                    cv2.circle(img, (x2, y2), 4, (50, 200, 255), cv2.FILLED)
                    cv2.circle(img, (x2, y2), 8, (50, 200, 255), 2)
                    cv2.circle(img, (x3, y3), 4, (50, 200, 255), cv2.FILLED)
                    cv2.circle(img, (x3, y3), 8, (50, 200, 255), 2)
                    cv2.putText(img, str(int(angle)), (500, 100),
                                cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), 2)

                else:
                    # Desenhar linha de conecção entre os pontos
                    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
                    cv2.line(img, (x3, y3), (x2, y2), (0, 255, 0), 3)

                    # Desenhar 2 circulos entre os marcadores de interesse
                    cv2.circle(img, (x1, y1), 4, (255, 0, 0), cv2.FILLED)
                    cv2.circle(img, (x1, y1), 8, (255, 0, 0), 2)
                    cv2.circle(img, (x2, y2), 4, (255, 0, 0), cv2.FILLED)
                    cv2.circle(img, (x2, y2), 8, (255, 0, 0), 2)
                    cv2.circle(img, (x3, y3), 4, (255, 0, 0), cv2.FILLED)
                    cv2.circle(img, (x3, y3), 8, (255, 0, 0), 2)
                    cv2.putText(img, str(int(angle)), (500, 100),
                                cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), 2)

            # Teste 2
            elif self.teste == 2:
                if self.teste == 2 and (90 - self.var < angle < 91 + self.var or 180 - self.var < angle < 180 or 
                                        30 - self.var < angle < 31 + self.var):
                    # Desenhar linha de conecção entre os pontos
                    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.line(img, (x3, y3), (x2, y2), (0, 0, 255), 3)

                    # Desenhar 2 circulos entre os marcadores de interesse
                    cv2.circle(img, (x1, y1), 4, (50, 200, 255), cv2.FILLED)
                    cv2.circle(img, (x1, y1), 8, (50, 200, 255), 2)
                    cv2.circle(img, (x2, y2), 4, (50, 200, 255), cv2.FILLED)
                    cv2.circle(img, (x2, y2), 8, (50, 200, 255), 2)
                    cv2.circle(img, (x3, y3), 4, (50, 200, 255), cv2.FILLED)
                    cv2.circle(img, (x3, y3), 8, (50, 200, 255), 2)
                    cv2.putText(img, str(int(angle)), (500, 100),
                                cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), 2)

                else:
                    # Desenhar linha de conecção entre os pontos
                    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
                    cv2.line(img, (x3, y3), (x2, y2), (0, 255, 0), 3)

                    # Desenhar 2 circulos entre os marcadores de interesse
                    cv2.circle(img, (x1, y1), 4, (255, 0, 0), cv2.FILLED)
                    cv2.circle(img, (x1, y1), 8, (255, 0, 0), 2)
                    cv2.circle(img, (x2, y2), 4, (255, 0, 0), cv2.FILLED)
                    cv2.circle(img, (x2, y2), 8, (255, 0, 0), 2)
                    cv2.circle(img, (x3, y3), 4, (255, 0, 0), cv2.FILLED)
                    cv2.circle(img, (x3, y3), 8, (255, 0, 0), 2)
                    cv2.putText(img, str(int(angle)), (500, 100),
                                cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), 2)

            # Teste 3
            elif self.teste == 3:
                if self.teste == 3 and (90 - self.var < angle < 91 + self.var or 180 - self.var < angle < 180 or 
                                        30 - self.var < angle < 31 + self.var or 45 - self.var < angle < 41 + self.var):
                    # Desenhar linha de conecção entre os pontos
                    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cv2.line(img, (x3, y3), (x2, y2), (0, 0, 255), 3)

                    # Desenhar 2 circulos entre os marcadores de interesse
                    cv2.circle(img, (x1, y1), 4, (50, 200, 255), cv2.FILLED)
                    cv2.circle(img, (x1, y1), 8, (50, 200, 255), 2)
                    cv2.circle(img, (x2, y2), 4, (50, 200, 255), cv2.FILLED)
                    cv2.circle(img, (x2, y2), 8, (50, 200, 255), 2)
                    cv2.circle(img, (x3, y3), 4, (50, 200, 255), cv2.FILLED)
                    cv2.circle(img, (x3, y3), 8, (50, 200, 255), 2)
                    cv2.putText(img, str(int(angle)), (500, 100),
                                cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), 2)

                else:
                    # Desenhar linha de conecção entre os pontos
                    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
                    cv2.line(img, (x3, y3), (x2, y2), (0, 255, 0), 3)

                    # Desenhar 2 circulos entre os marcadores de interesse
                    cv2.circle(img, (x1, y1), 4, (255, 0, 0), cv2.FILLED)
                    cv2.circle(img, (x1, y1), 8, (255, 0, 0), 2)
                    cv2.circle(img, (x2, y2), 4, (255, 0, 0), cv2.FILLED)
                    cv2.circle(img, (x2, y2), 8, (255, 0, 0), 2)
                    cv2.circle(img, (x3, y3), 4, (255, 0, 0), cv2.FILLED)
                    cv2.circle(img, (x3, y3), 8, (255, 0, 0), 2)
                    cv2.putText(img, str(int(angle)), (500, 100),
                                cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), 2)


        return angle


# Quando quiser ver do que um módulo é capaz ou o roteiro
def main():
    return

# verificar se o programa está sendo executado por si só
if __name__ == "__main__":
    main()
