# AMPR (so cool)

from cv2 import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\ETG30\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

filename = "car_number_plate.png"

img = cv2.imread(fr"C:\Users\ETG30\OneDrive\Desktop\Python\OpenCV\temp_env\OpenCV\Resources\{filename}")
print(img.shape)

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
imgOutGray = cv2.cvtColor(imgOut, cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(imgOutGray,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Extracted image", imgOut)
cv2.imshow("Binarized image", thresh1)


print(pytesseract.image_to_string(thresh1))

# C:\Users\ETG30\AppData\Local\Programs\Tesseract-OCR

cv2.waitKey(0)