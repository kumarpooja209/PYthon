import cv2


img=cv2.imread("abc.jpg")

cv2.imshow("Hello",img)

cv2.waitKey(0)

print(img.shape)

print("Height of the image",int(img.shape[0]),"pixels")
print("width of the image",int(img.shape[1]),"pixels")

cv2.imwrite("Output.jpg",img)
cv2.imwrite("Output.png",img)


cv2.destroyAllWindows()
