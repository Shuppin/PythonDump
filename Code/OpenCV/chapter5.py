# AMPR (so cool)
from cv2 import cv2
import numpy as np

filename = "car_number_plate.png"

img = cv2.imread(f"Resources/{filename}")
#print(img.shape)

coords = [(229,214),(330,172),(234,242),(332,199)]

width, height = 500,100

points1 = np.float32([[229,214],[330,172],[234,242],[332,199]])
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(points1, points2)

imgOut = cv2.warpPerspective(img, matrix,(width,height))

cv2.line(img,coords[0],coords[1],(0,255,255),2)
cv2.line(img,coords[0],coords[2],(0,255,255),2)
cv2.line(img,coords[3],coords[2],(0,255,255),2)
cv2.line(img,coords[3],coords[1],(0,255,255),2)

cv2.circle(img,coords[0],4,(0,0,255),cv2.FILLED)
cv2.circle(img,coords[1],4,(0,0,255),cv2.FILLED)
cv2.circle(img,coords[2],4,(0,0,255),cv2.FILLED)
cv2.circle(img,coords[3],4,(0,0,255),cv2.FILLED)

cv2.imshow(filename, img)
cv2.imshow("Extracted image", imgOut)

cv2.waitKey(0)