import cv2
import numpy as np

img=np.zeros((512,512),np.uint8)+100 #0 itu adalah hitam
img2=np.zeros((512,512,3),np.uint8) #uint8 untuk mengubah tipe data dari 1 menjadi 255
img3=np.zeros((256,512))

#cv2.imshow("img",img)
#cv2.imshow("img2",img2)
#cv2.imshow("img3",img3)

img2[:256,:256]=255,0,0
img2[:256,256:]=0,255,0
img2[256:,:256]=0,0,255
img2[256:,256:]=100,100,100

cv2.imshow("img2",img2)
cv2.waitKey(0)

