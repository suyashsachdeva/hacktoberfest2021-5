import cv2 as cv 
import numpy as np


def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width/2,height/2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width,height)

    return cv.warpAffine(img, rotMat, dimension) 
     
#link = r'C:\Users\suyash\Desktop\WhatsApp Video 2021-04-27 at 00.54.28.mp4'
cap = cv.VideoCapture(0)
i = 0
while True:
    
    ret, frame=cap.read()
    i=i+1
    rot = rotate(frame , i)
    cv.imshow('frame',rot)
    if i>179:
        i=-180
    if cv.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv.destroyAllWindows()
