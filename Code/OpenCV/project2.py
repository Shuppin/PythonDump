from cv2 import cv2
import numpy as np

kernel = np.ones((5,5))

imWidth = 480
imHeight = 480
imScale = 0.7
imWidth = imWidth * imScale
imHeight = imHeight * imScale

print(540.32//1)

imWidth = int(imWidth//1)
imHeight = int(imHeight//1)

#print(imWidth,imHeight)

#cam = cv2.VideoCapture(0)
#cam.set(3,640)
#cam.set(4,480)

img = cv2.imread("C:\\Users\\ETG30\\OneDrive\\Desktop\\Python\\OpenCV\\temp_env\\OpenCV\\Resources\\cardA.png")

#def preProcessing(image):
#    imgGrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#    imgBlur = cv2.GaussianBlur(imgGrey, (5,5),1)
#    imgCanny = cv2.Canny(imgBlur,200,200)
#    imgDail = cv2.dilate(imgCanny,kernel,iterations=2)
#    imgThres = cv2.erode(imgDail,kernel,iterations=1)
#
#    return imgThres

def getContours(image):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            #cv2.drawContours(imgCont, cnt, -1, (255,0,0),3)
            perim = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt,0.02*perim,True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(imgCont, biggest, -1, (255,0,0),20)
    return biggest


def reorder(points):
    points = points.reshape((4,2))
    pointsNew = np.zeros((4,1,2),np.int32)
    add = points.sum(1)

    pointsNew[0] = points[np.argmin(add)]
    pointsNew[3] = points[np.argmax(add)]
    diff = np.diff(points,axis=1)
    pointsNew[1] = points[np.argmin(diff)]
    pointsNew[2] = points[np.argmax(diff)]
    
    return pointsNew

    

def getWarp(image, biggest):
    biggest = reorder(biggest)
    points1 = np.float32(biggest)
    points2 = np.float32([[0,0],[imWidth,0],[0,imHeight],[imWidth,imHeight]])
    matrix = cv2.getPerspectiveTransform(points1, points2)

    imgOut = cv2.warpPerspective(img, matrix,(imWidth,imHeight))

    imgCropped = imgOut[10:imgOut.shape[0]-10,10:imgOut.shape[1]-10]
    imgCropped = cv2.resize(imgCropped,(imWidth, imHeight))

    return imgCropped

while True:
    #sucess, img = cam.read()
    
    img = cv2.resize(img,(imWidth,imHeight))
    imgBlank = np.zeros_like(img)
    imgWarpedBlank = np.zeros_like(img)
    imgCont = img.copy()
    #imgThreshold = preProcessing(img)
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGrey, (5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    imgDail = cv2.dilate(imgCanny,kernel,iterations=2)
    imgThres = cv2.erode(imgDail,kernel,iterations=1)
    biggest = getContours(imgThres)
    grey_3_channel = cv2.cvtColor(imgGrey, cv2.COLOR_GRAY2BGR)
    imgCanny_3_channel = cv2.cvtColor(imgCanny, cv2.COLOR_GRAY2BGR)
    imgThres_3_channel = cv2.cvtColor(imgThres, cv2.COLOR_GRAY2BGR)


    if biggest.size != 0:
        imgWarped = getWarp(img, biggest)

        imgWarpedGrey = cv2.cvtColor(imgWarped, cv2.COLOR_BGR2GRAY)
        imgWarpedGreyCanny = cv2.Canny(imgWarpedGrey,200,200)

        imgWarpedGrey_3_channel = cv2.cvtColor(imgWarpedGrey, cv2.COLOR_GRAY2BGR)
        imgWarpedGreyCanny_3_channel = cv2.cvtColor(imgWarpedGreyCanny, cv2.COLOR_GRAY2BGR)

        imgWarpedGreyCanny_3_channel = cv2.bitwise_not(imgWarpedGreyCanny_3_channel)

        imgStackHor1 = np.hstack((img, grey_3_channel, imgCanny_3_channel, imgCont))
        imgStackHor2 = np.hstack((imgWarped, imgWarpedGrey_3_channel, imgWarpedGreyCanny_3_channel, imgBlank))

        imgStack = np.vstack((imgStackHor1,imgStackHor2))

        cv2.rectangle(img,(0,0),(150,30),(0,0,0),cv2.FILLED)
        cv2.putText(img, "Raw input", (10,20),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)

        cv2.rectangle(grey_3_channel,(0,0),(150,30),(0,0,0),cv2.FILLED)
        cv2.putText(grey_3_channel, "Greyscale", (10,20),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)

        cv2.rectangle(imgCanny_3_channel,(0,0),(150,30),(0,0,0),cv2.FILLED)
        cv2.putText(imgCanny_3_channel, "Edgeified", (10,20),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)

        cv2.imshow("frame 0", imgStack)

        #cv2.imshow("frame 0", img)
        #cv2.imshow("frame 1", imgThres)
        #cv2.imshow("frame 2", imgCont)
        #cv2.imshow("frame 3", imgWarped)
    else:

        cv2.putText(imgWarpedBlank, "No document", (imWidth//2-85,imHeight//2),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)

        imgStackHor1 = np.hstack((img, grey_3_channel, imgCanny_3_channel, imgCont))
        imgStackHor2 = np.hstack((imgWarpedBlank, imgBlank, imgBlank, imgBlank))

        imgStack = np.vstack((imgStackHor1,imgStackHor2))

        cv2.imshow("frame 0", imgStack)

        #cv2.imshow("frame 0", img)
        #cv2.imshow("frame 1", imgThres)
        #cv2.imshow("frame 2", imgCont)
        #cv2.putText(imgBlank, "No document", (imWidth//2-85,imHeight//2),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)
        #cv2.imshow("frame 3", imgBlank)
        
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

