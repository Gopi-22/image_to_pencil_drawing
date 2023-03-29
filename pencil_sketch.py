import cv2
import numpy as np
img=cv2.imread("car.jpg")

resize = cv2.resize(img,(0,0),fx=0.4,fy=0.4)

gray_img=cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
invert=cv2.bitwise_not(gray_img)
blur=cv2.GaussianBlur(invert,(21,21),0)
invertedblur=cv2.bitwise_not(blur)
sketch=cv2.divide(gray_img,invertedblur,scale=200)



cv2.imshow("Image",sketch)
cv2.waitKey(6000)
cv2.destroyAllWindows()

status=cv2.imwrite("car1.jpeg",sketch)
print("Image written  to file-system",status)
