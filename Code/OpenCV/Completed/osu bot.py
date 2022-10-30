import numpy as np

import cv2

from mss.windows import MSS as mss
from PIL import Image

#import keyboard
from pynput.mouse import Button, Controller
mouse = Controller()

import time
import random
import sys
 
def getObjects(image):
    """
    Image must be of canny fomat (cv2.Canny(rgb_image))
    """

    posList = []

    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    objCounter = 0
    for cnt in contours:
        #print(type(cnt),len(cnt))
        area = cv2.contourArea(cnt)
        #print("-----------------------------")
        #print("Shape", cnt)
        #print("Area is", area)
        if area > 5000:
            cv2.drawContours(imgContour, cnt, -1, (255,0,0),3)
            perim = cv2.arcLength(cnt, True)
            #print("Perimeter is", perim)
            approx = cv2.approxPolyDP(cnt,0.02*perim,True)
            #print("Corner points:", len(approx))
            objCorners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            x_pos = x+w//2
            y_pos = y+h//2

            if objCorners == 4:
                aspRatio = w/float(h)
                if 1.15 > aspRatio > 0.85:
                    objectType = "Modifier"
                else:
                    objectType = "Button"

            elif objCorners > 4:
                if h > 550:
                    objectType = f"Spinner"
                    cv2.rectangle(imgContour,(x-100,y),(x+w+100,y+h),(0,255,255),2)
                else:
                    aspRatio = w/float(h)
                    if 1.15 > aspRatio > 0.85:
                        objectType = f"Circle"
                        cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,0,255),2)
                        #if range(x_pos-5,x_pos+5) not in posList and range(y_pos-5,y_pos+5) not in posList:
                        #    mouse.position = (x+w//2, y+h//2)
                        #    posList.append(x+w//2)
                        #    posList.append(y+h//2)
                    else:
                        objectType = f"Slider"
                        cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
                        #mouse.position = (y+h//2, x+w//2)
                    objCounter = objCounter + 1

            else:
                objectType = "nul"
                print("nul object found at", x,y)

            #cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            if objectType == "Modifier":
                cv2.putText(imgContour, objectType, (x+10,y+25),cv2.FONT_HERSHEY_DUPLEX,0.6,(0,0,0),2)
            else:
                cv2.putText(imgContour, objectType, (x+10,y+25),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)

    return objCounter

count = 0

mon = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

sct = mss()

sWidth = 1920//2.3
sHeight = 1080//2.3

objList = []

while 1:
    sct_img = sct.grab(mon)
    # Create the Image
    imgPIL = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
    img = np.array(imgPIL)
    imgSmall = cv2.resize(img, (int(sWidth), int(sHeight)))
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    greySmall = cv2.resize(grey, (int(sWidth), int(sHeight)))
    grey_3_channel = cv2.cvtColor(greySmall, cv2.COLOR_GRAY2BGR)
    imgContour = img.copy()
    imgBlank = np.zeros_like(img)
    imgBlur = cv2.GaussianBlur(grey,(7,7),1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)
    imgCannySmall = cv2.resize(imgCanny,(int(sWidth), int(sHeight)))
    imgCanny_3_channel = cv2.cvtColor(imgCannySmall, cv2.COLOR_GRAY2RGB)

    #cv2.imshow('frame 0', imgSmall)
    #cv2.imshow('frame 1', imgCannySmall)

    objCounter2 = 0
    objCounter2 = getObjects(imgCanny)
    if objCounter2 is not None:
        objList.append(objCounter2)


    imgContourSmall = cv2.resize(imgContour, (int(sWidth), int(sHeight)))

    objListHighest = str(max(objList))

    cv2.rectangle(imgContourSmall,(0,0),(300,70),(0,0,0),cv2.FILLED)
    cv2.putText(imgContourSmall, "Final result", (10,20),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)
    cv2.putText(imgContourSmall, f"Current Objects: {str(objCounter2)}", (10,40),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)
    cv2.putText(imgContourSmall, f"Max Objects: {objListHighest}", (10,60),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)

    cv2.rectangle(imgSmall,(0,0),(150,30),(0,0,0),cv2.FILLED)
    cv2.rectangle(grey_3_channel,(0,0),(250,30),(0,0,0),cv2.FILLED)
    cv2.rectangle(imgCanny_3_channel,(0,0),(270,30),(0,0,0),cv2.FILLED)

    cv2.putText(imgSmall, "Raw input", (10,20),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)
    cv2.putText(grey_3_channel, "Greyscale image", (10,20),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)
    cv2.putText(imgCanny_3_channel, "Edgeified (Binary)", (10,20),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)

    imgStackHor1 = np.hstack((imgSmall, grey_3_channel))
    imgStackHor2 = np.hstack((imgCanny_3_channel, imgContourSmall))
    imgStack = np.vstack((imgStackHor1,imgStackHor2))

    cv2.imshow('frame 0', imgStack)
    cv2.imshow('frame 1', imgContourSmall)
    
    cv2.waitKey(10)
    #while True:
    #if cv2.waitKey(0) & 0xFF == ord('q'):
    #    print("Capturing frame...")
    #    cv2.destroyAllWindows()
    #    break

    if len(objList) > 20000:
        objList = []

    #if keyboard.is_pressed("Esc"):
    #    print("Keyboard Interrupt")
    #    sys.exit()

    #cv2.destroyAllWindows()
    count = count + 1

    