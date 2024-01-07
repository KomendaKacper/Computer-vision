import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import time
import autopy

cap = cv2.VideoCapture(0)

wCam, hCam = 640,480
cap.set(3, wCam)
cap.set(4, hCam)
detector = HandDetector(detectionCon=0.8)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    allHands, img = detector.findHands(img, flipType=False, draw = True)
    if len(allHands) != 0:
        hand = allHands[0]
        lmList = hand["lmList"]

        if len(lmList)!= 0:
            x1,y1 = lmList[8][:2]
            x2,y2 = lmList[12][:2]

            print (x1,y1,x2,y2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)