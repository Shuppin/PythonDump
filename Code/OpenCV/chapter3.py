# Cropping & Resizing

from cv2 import cv2
import numpy as np

img = cv2.imread("Resources/face.png")
smallImg = cv2.resize(img, (512, 288))
croppedImg = img[0:200, 200:500]

shape = img.shape
smallShape = smallImg.shape
croppedShape = croppedImg.shape

print(f"Width: {shape[0]} \nHeight: {shape[1]} \nLayers: {shape[2]}")

cv2.imshow(f"face.png ({shape[0]}x{shape[1]})", img)
cv2.imshow(f"face.png ({smallShape[0]}x{smallShape[1]})", smallImg)
cv2.imshow(f"face.png ({croppedShape[0]}x{croppedShape[1]})", croppedImg)

cv2.waitKey(0)