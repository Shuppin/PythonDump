from cv2 import cv2
import numpy as np
import imutils
import resize_image

# Read image
img = cv2.imread(r"C:\Users\ETG30\OneDrive\Desktop\Python\OpenCV\anpr\resources\car_number_plate_2.png")

# Make sure image isn't huge
_, width, _ = img.shape

if width > 1920:
    print("Image is very large, resizing")
    img = resize_image.resize(img, height=1920)

# Simplify image to better detect edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.bilateralFilter(gray, 13, 15, 15)

# Detect edges
edged = cv2.Canny(gray, 30, 200)

# Detect contours (Closed shapes within edges)
contours, hierarchy=cv2.findContours(edged.copy(),cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours,key=cv2.contourArea, reverse = True)[:10]
screenCnt = []
counter = 0

# Iterate over the 10 largest contours and select which ones are rectangle shapes
#while screenCnt is not None:
#    for c in contours:
#        # approximate the contour
#        peri = cv2.arcLength(c, True)
#        approx = cv2.approxPolyDP(c, counter * peri, True)
#        # if our approximated contour has four points, then
#        # we can assume that we have found our screen
#        if len(approx) == 4:
#            screenCnt = approx
#            break
#        counter += 0.001
#        print(counter)
#    break


for contour, hier in zip(contours, hierarchy):
    (x,y,w,h) = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

print(screenCnt)

imgContour = cv2.polylines(edged, screenCnt, True, (255,0,0), 10)

cv2.imshow("anpr", )

if screenCnt is not None:
    cv2.waitKey(0)