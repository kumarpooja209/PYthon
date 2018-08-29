import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)


cv2.imshow('Image',img)
cv2.line(img,(0,0),(511,511),(255,127,0),5)
cv2.imshow('Blue line',img)

cv2.waitKey()
cv2.destroyAllWindows()
