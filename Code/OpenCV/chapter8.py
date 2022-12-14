from cv2 import cv2
import numpy as np

def _stackImages(scale,imgArray):
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

def getContours(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print("-----------------------------")
        #print("Shape", cnt)
        print("Area is", area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255,0,0),3)
            perim = cv2.arcLength(cnt, True)
            #print("Perimeter is", perim)
            approx = cv2.approxPolyDP(cnt,0.02*perim,True)
            print("Corner points:", len(approx))
            objCorners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCorners == 3:
                objectType = "Triangle"

            elif objCorners == 4:
                aspRatio = w/float(h)
                if 1.05 > aspRatio > 0.95:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"

            elif objCorners > 4:
                objectType = "Circle"

            else:
                objectType = "nul"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour, objectType, (x+10,y+25),cv2.FONT_HERSHEY_DUPLEX,0.8,(0,0,0),2)


cap1 = cv2.VideoCapture(0)
cap1.set(3,640)
cap1.set(4,480)


while True:

    success, img = cap1.read()

    imgContour = img.copy()

    imgBlank = np.zeros_like(img)
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)

    getContours(imgCanny)

    #imgStack = _stackImages(0.7,([img,imgGray,imgBlur],[imgCanny,imgContour,imgBlank]))

    cv2.imshow("webcam 0 (Stacked)", imgStack)

    cv2.waitKey(0)