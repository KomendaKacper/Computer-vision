import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)
coloR = (255, 0, 255)

cx, cy, w, h = 100, 100, 200, 200 


class DragRect():
    def __init__(self, posCenter, size = [200, 200]):
        self.posCenter = posCenter
        self.size = size

    def update(self, cursor):
        cx,cy = self.posCenter
        w,h = self.size

        if cx-w//2 < cursor[0]< cx+w//2 and cy-h//2 < cursor[1] < cy+h//2:
            self.posCenter = cursor
rectList = []
for x in range(5):           
    rectList.append (DragRect([x*250 + 150,150]))
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    allHands, img = detector.findHands(img, flipType= False, draw = False)    
    
    if allHands:
        hand = allHands[0]
        #print (hand)
        lmList = hand["lmList"]
        
        length, info, img = detector.findDistance((lmList[8][0],lmList[8][1]),(lmList[4][0],lmList[4][1]),img)
        cv2.putText(img, "Odleglosc: " + str(int (length)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,255),3)
        if length < 40:
            cursor = [lmList[8][0], lmList[8][1]] 
            for rect in rectList:  
                rect.update(cursor)
    """
    draw solid
    for rect in rectList:
        cx,cy = rect.posCenter
        w,h = rect.size
        cv2.rectangle(img, (cx-w//2, cy-h//2), (cx+w//2, cy+h//2), coloR , cv2.FILLED)
        cvzone.cornerRect(img,(cx-w//2, cy-h//2, w, h), 20, rt=0)
"""
    #draw Transperency
    imgNew = np.zeros_like(img, np.uint8)
    for rect in rectList:
        cx, cy = rect.posCenter
        w, h = rect.size
        cv2.rectangle(imgNew, (cx - w // 2, cy - h // 2),
                      (cx + w // 2, cy + h // 2), coloR, cv2.FILLED)
        cvzone.cornerRect(imgNew, (cx - w // 2, cy - h // 2, w, h), 20, rt=0)

    out = img.copy()
    alpha = 0.5
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
    
    cv2.imshow("Image", out)
    cv2.waitKey(1)

