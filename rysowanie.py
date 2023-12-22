import numpy as np
import cv2

cap = cv2.VideoCapture(0) #0 - indeks kamerki której chcę użyć, można podać nazwę pliku z filmem

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10) #początek, koniec, kolory, grubość linii
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5) #początek, koniec, kolory, grubość linii
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5) #grubość = -1 oznacza wypełnienie
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1) #kordy środka, promień, kolor, grubość

    font = cv2.FONT_ITALIC #czcionka
    img = cv2.putText(img, 'Mega spoko ziomek', (10, height - 10), font, 2,  (0,0,0,), 5,  cv2.LINE_AA) #wybieram lewy dolny róg początku napisu
    #cv2.LINE_AA MAKES TEXT LOOKS BETTER
    #font, 4 to wielkość czcionki

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows

