import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)

#cv2.imshow('Image',img)
pts=np.array([[100,100],[250,100],[400,100]],np.int32)
pts1=np.array([[100,250],[250,50],[400,250]],np.int32)
cv2.polylines(img,[pts],True,(0,255,0),3)
cv2.polylines(img,[pts1],True,(0,255,0),3)

cv2.imshow('triangle',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

