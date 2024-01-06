import cv2
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
import time

cap = cv2.VideoCapture(0)

class DragRect():
    def __init__(self, posCenter, size):
        self.posCenter = posCenter
        self.size = size

    def update(self, cursor):
        cx,cy = self.posCenter
        w,h = self.size

rectList = []

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    detector = HandDetector(detectionCon = 0.8, maxHands= 2)
    Allhands, img = detector.findHands(img, draw=False, flipType=False)
    if Allhands:
        hand1 = Allhands[0]
        lmList1 = hand1["lmList"]
        p1 = lmList1[8][0],lmList1[8][1]

        if len(Allhands) == 2:
            hand2 = Allhands[1]
            lmList2 = hand2["lmList"]
            p2 = lmList2[8][0],lmList2[8][1]

            length = ((p1[0]-p2[0])**2+(p1[1]-p1[1])**2)**0.5
            
            cv2.circle(img, p1, 5, (0,0,255), cv2.FILLED)
            cv2.circle(img, p2, 5, (0,0,255), cv2.FILLED)

            cv2.rectangle(img, p1, p2, (255,0,255), 3)

            x1, y1 = lmList1[8][0], lmList1[8][1]
            x2, y2 = lmList2[8][0], lmList2[8][1]

            if ((lmList2[11][0]-lmList2[8][0])**2+(lmList2[11][1]-lmList2[8][1])**2)**0.5 < 30 and ((lmList1[11][0]-lmList1[8][0])**2+(lmList1[11][1]-lmList1[8][1])**2)**0.5 < 30:
                rectList.append(DragRect([x1, y1], [abs(x1-x2), abs(y1-y2)]))
                time.sleep(0.3)
    
    if len(rectList) != 0:            
        for rect in rectList:
            cx, cy = rect.posCenter
            w, h = rect.size
            cv2.rectangle(img, (cx,cy), (cx+w,cy+h), (0,255,0), cv2.FILLED)

    cv2.imshow("Image", img)
    cv2.waitKey(1)