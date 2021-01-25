import cv2
import numpy as np

img = cv2.imread("gambarbaru.png")
imgresized = cv2.resize(img, (300, 400))

#cv2.imshow("gambar 1", img)
#cv2.imshow("gambar 2", imgresized)
#cv2.waitKey(0)

#imggray = cv2.cvtColor(imgresized, cv2.COLOR_BGR2GRAY)
#imgblur9 = cv2.GaussianBlur(imgresized, (9,9), 10)
#imgblur99 = cv2.GaussianBlur(imgresized, (99,99), 10)
#imgcanny = cv2.Canny(img,150,200)
#imgcanny5 = cv2.Canny(img,150,300)

#kernel = np.ones((5,5),np.uint8)
#imgDilation = cv2.dilate(imgcanny,kernel,iterations=1)
#imgEroded = cv2.erode(imgcanny,kernel,iterations=1)
#imgEroded2 = cv2.erode(img,kernel,iterations=1)
imgcropped = img[0:200,0:200]


cv2.imshow("img",img)
#cv2.imshow("gray", imggray)
#cv2.imshow("blur9", imgblur9)
#cv2.imshow("blur99", imgblur99)
#cv2.imshow("imgcanny", imgcanny)
#cv2.imshow("imgcanny5", imgcanny5)
#cv2.imshow("dilat",imgDilation)
#cv2.imshow("eroded",imgEroded)
#cv2.imshow("eroded2",imgEroded2)
cv2.imshow("crop",imgcropped)
cv2.waitKey(0)
