import cv2
import numpy as np

img=cv2.imread('abc.jpg')

cv2.imshow('Original',img)
cv2.waitKey(0)

img_scaled=cv2.resize(img,None,fx=0.75,fy=.75)
cv2.imshow('Scaling Linear',img_scaled)
cv2.waitKey()

img_scaled1=cv2.resize(img,None,fx=2,fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Scaling Cubic',img_scaled1)
cv2.waitKey()

img_scaled2=cv2.resize(img,(900,400), interpolation=cv2.INTER_AREA)
cv2.imshow('Scaling Skwed',img_scaled2)
cv2.waitKey()

