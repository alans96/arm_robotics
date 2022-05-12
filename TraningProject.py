import cv2
import numpy as np
import PoseModule as pm
from openpyxl import Workbook

cap = cv2.VideoCapture(0)  # Fonte da imagem
fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # Fonte da para gravação
out = cv2.VideoWriter('test_r.avi', fourcc, 20.0, (640, 480))  # Formato do vídeo

# Criação do excel
wb = Workbook()
# workbook_name = "Left_Arm.xlsx"
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
        # Detectar o corpo e marcadores sem desenhar
        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)

        # Lista de marcadores
        if len(lmList) != 0:
            try:
                # Right Arm
                angle = detector.findAngle(img, 11, 13, 15)
                # fazer o angulo converter de 0 a 100
                per = np.interp(angle, (40, 171), (0, 100))

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
                # Número da repetição
                cv2.putText(img, str(int(count)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

                # Excel
                wb1.append([lmList[11][1], lmList[11][2], lmList[13][1], lmList[13][2],
                            lmList[15][1], lmList[15][2], angle])

            """try:
                # Left Arm
                angle = detector.findAngle(img, 12, 14, 16)
                # fazer o angulo converter de 0 a 100
                per = np.interp(angle, (217, 315), (0, 100))
                
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
