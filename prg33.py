import cv2
import numpy as np


square=np.zeros((300,300), np.uint8)


cv2.rectangle(square,(50,50),(250,250),255,-1)
cv2.imshow("square",square)
cv2.waitKey(0)


ellipse=np.zeros((300,300), np.uint8)


cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow("ellipse",ellipse)
cv2.waitKey(0)

And=cv2.bitwise_and(square,ellipse)
cv2.imshow("And",And)
cv2.waitKey(0)

Or=cv2.bitwise_or(square,ellipse)
cv2.imshow("Or",Or)
cv2.waitKey(0)

Xor=cv2.bitwise_xor(square,ellipse)
cv2.imshow("Xor",Xor)
cv2.waitKey(0)

Not=cv2.bitwise_not(square,ellipse)
cv2.imshow("Not",Not)
cv2.waitKey(0)

cv2.destroyAllWindows()
