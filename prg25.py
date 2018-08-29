import cv2
import numpy as np

img=cv2.imread("abc.jpg")
cv2.imshow('Original',img)
height, width=img.shape[:2]

r_matrix=cv2.getRotationMatrix2D((width/2,height/2),70,.7)

r_image=cv2.warpAffine(img,r_matrix,(width,height))

cv2.imshow("Rotated",r_image)
cv2.imshow('Original',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
