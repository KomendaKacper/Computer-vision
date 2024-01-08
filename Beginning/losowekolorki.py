import cv2
import random
import numpy

img = cv2.imread('major.jpg',-1)

print (img.shape) #wysokość, szerokość, kanały(bgr)
#print (img[0][10:100]) #1wszy rząd, 10-100 kolumny kolorki

for i in range (100):
    for j in range (img.shape[1]):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('major.jpg',-1)
tag = img[50:100, 100:150] #rzędy, kolumny
img[30:80, 150:200] = tag

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()