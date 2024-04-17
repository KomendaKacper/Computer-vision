import cv2

img = cv2.imread('major.jpg',1)
img = cv2.resize(img, (0,0), fx=2,fy=2) #2 razy większe niż oryginał
img = cv2.rotate (img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite('new_img.jpg', img)

cv2.imshow('NazwaOkna',img)
cv2.waitKey(0)
cv2.destroyAllWindows()