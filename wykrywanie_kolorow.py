import numpy as np
import cv2

cap = cv2.VideoCapture(0) #0 - indeks kamerki której chcę użyć, można podać nazwę pliku z filmem

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Hue Saturation Value - odcień, nasycenie koloru i moc światła białego
    lower_blue = np.array([90, 50, 50]) #jasny niebieski
    upper_blue = np.array([130, 255, 255]) #ciemny niebieski

    mask = cv2.inRange(hsv, lower_blue, upper_blue) #podświetla tylko niebieski

    result = cv2.bitwise_and(frame, frame, mask = mask) #Zaczernia wszystko co nie jest niebieskie


    cv2.imshow('result', result)    
    cv2.imshow('mask', mask)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows

BGR_color = np.array([[[255, 0, 0]]])
x = cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)
x[0][0] #Daje jeden pixel

#yooooooooooooooooooooooooo