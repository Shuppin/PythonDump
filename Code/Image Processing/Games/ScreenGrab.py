import numpy as np
from PIL import ImageGrab
import cv2

SCALE = 0.5
# RES LIST 1280*720, 1920*1080
RES_BBOX = (0,0,1920,1080)

#print(keys.dk."1")

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def img_process(image):
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=300, threshold2=200)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    verts = np.array([[20,720],[430,350],[850,350],[1260,720]])
    #processed_img = roi(hsv, [verts])
    return processed_img

while True:
    screen  = np.array(ImageGrab.grab(bbox=RES_BBOX))
    #canny = img_process(screen)

    cv2.namedWindow("Screen(1280x720) Canny", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Screen(1280x720) Canny", (int((1280*SCALE)), int((720*SCALE))))
    cv2.imshow('Screen(1280x720) Canny', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
