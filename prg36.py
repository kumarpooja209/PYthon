import cv2
import numpy as np



img=cv2.imread("abc.jpg")
cv2.imshow('Orginal ',img)
cv2.waitKey(0)

blur=cv2.blur(img,(3,3))
cv2.imshow('Blur image',blur)
cv2.waitKey(0)



Gaussian=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow('Gaussian Blur image',Gaussian)
cv2.waitKey(0)


median=cv2.medianBlur(img,5)
cv2.imshow('Median Blur image',median)
cv2.waitKey(0)


bilateral=cv2.bilateralFilter(img,9,75,75)
cv2.imshow('Bilateral image',bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()
