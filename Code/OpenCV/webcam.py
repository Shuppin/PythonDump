#import numpy.core.multiarray
from cv2 import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)

cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)
#cap.set(10,100)

while True:

    success, img = cap.read()


    imgCanny = cv2.Canny(img, 100, 100)
    cv2.imshow("webcam 0 (Canny Edge Detection)", imgCanny)

    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)
    #cv2.imshow("webcam 0 (Dilation)", imgDil)

    imgEroded = cv2.erode(imgDil, kernel, iterations=1)
    #cv2.imshow("webcam 0 (Errosion)")

    #cv2.imshow("webcam 0 (Dilation & Erosion & Canny Edge Detection)", imgEroded)

    cv2.imshow("webcam 0", img)


    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break