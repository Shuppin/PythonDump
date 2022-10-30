from cv2 import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def empty(x):
    pass

cap0 = cv2.VideoCapture(0)
cap0.set(3,640)
cap0.set(4,480)

cap1 = cv2.VideoCapture(1)
cap1.set(3,640)
cap1.set(4,480)


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)  # Reflective Yellow configuration
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 105, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 74, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)


while True:
    success, img0 = cap0.read()
    success, img1 = cap1.read()

    imgHSV0 = cv2.cvtColor(img0, cv2.COLOR_BGR2HSV)
    imgHSV1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    mask0 = cv2.inRange(imgHSV0,lower,upper)
    mask1 = cv2.inRange(imgHSV1,lower,upper)

    imgResult0 = cv2.bitwise_and(img0,img0,mask=mask0)
    imgResult1 = cv2.bitwise_and(img1,img1,mask=mask1)

    imgStack1 = stackImages(0.5,([img0,imgHSV0,img1,imgHSV1],[mask0,imgResult0,mask1,imgResult1]))

    cv2.imshow("webcam 0 & webcam 1 -  Filters  -= | Normal feed | HSV feed | Mask/Filter feed | Final result | =-", imgStack1)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break