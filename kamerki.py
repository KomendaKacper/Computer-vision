import numpy as np
import cv2

cap = cv2.VideoCapture(0) #0 - indeks kamerki której chcę użyć, można podać nazwę pliku z filmem

while True:
    ret, frame = cap.read()

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows

