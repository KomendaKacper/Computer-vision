import mediapipe as mp
import cv2
from cvzone.HandTrackingModule import HandDetector
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon = 0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]

while True:
    success, img = cap.read()
    
    hands,img = detector.findHands(img, draw = False)
    
    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        
        if len(lmList) != 0:
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]

            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            


            cv2.circle(img, (x1,y1), 15, (0,0,255), cv2.FILLED)
            cv2.circle(img, (x2,y2), 15, (0,0,255), cv2.FILLED)

            length = ((x1-x2)**2+(y1-y2)**2)**0.5

            cv2.putText(img, "Odleglosc: " + str(int(length)), (10,30), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,255), 2)



            vol = np.interp(length, [10, 200], [minVol, maxVol])
            volBar = np.interp(length, [10, 200], [400, 150])
            volPer = np.interp(length, [10, 200], [0, 100])
            print(int(length), vol)
            volume.SetMasterVolumeLevel(vol, None)
                
            cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
            cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
            cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)