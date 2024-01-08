import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import time
import autopy

cap = cv2.VideoCapture(0)

pTime = 0
plocX, plocY = 0,0
clocX, clocY = 0, 0

wCam, hCam = 640,480
cap.set(3, wCam)
cap.set(4, hCam)
detector = HandDetector(detectionCon=0.8)

wScr, hScr = autopy.screen.size()
#print (wScr, hScr)
frameR = 100
smoothening = 7

while True:
    success, img = cap.read()
    allHands, img = detector.findHands(img, flipType=True, draw = True)
    if len(allHands) != 0:
        hand = allHands[0]
        lmList = hand["lmList"]

        if len(lmList)!= 0:
            x1,y1 = lmList[8][:2]
            x2,y2 = lmList[12][:2]

            fingers = detector.fingersUp(hand)
            #print (fingers)
            cv2.rectangle(img, (frameR, frameR), (wCam-frameR, hCam-frameR),(255,0,255),2)
            if fingers[1] == 1 and fingers[2] == 0:
            
                x3 = np.interp(x1, (frameR,wCam-frameR), (0, wScr))
                y3 = np.interp(y1, (frameR,hCam-frameR), (0, hScr))

                clocX = plocX + (x3-plocX) / smoothening
                clocY = plocY + (y3-plocY) / smoothening
                

                autopy.mouse.move(wScr-clocX,clocY)
                cv2.circle(img,(x1,y1), 15, (255,0,255), cv2.FILLED)
                plocX, plocY = clocX, clocY

            if fingers[1] == 1 and fingers[2] == 1:
                length, info, img = detector.findDistance((x1,y1),(x2,y2),img)
                #print (length)

                if length < 30:
                    cv2.circle(img, (info[4],info[5]), 10, (0,255,0), cv2.FILLED)
                    autopy.mouse.click()

    cv2.imshow("Image", img)
    cv2.waitKey(1)