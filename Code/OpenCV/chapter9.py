from cv2 import cv2
#from cv2 import cv2

img_path = "C:\\Users\\ETG30\\OneDrive\\Desktop\\Python\\OpenCV\\temp_env\\OpenCV\\Resources\\face.png"
face_cascade_path = "C:\\Users\\ETG30\\OneDrive\\Desktop\\Python\\OpenCV\\temp_env\\OpenCV\\Resources\\Cascades\\haarcascade_frontalface_default.xml"
filename = "face.png"

faceCascade = cv2.CascadeClassifier(face_cascade_path)

img = cv2.imread(img_path)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow(filename, img)
cv2.waitKey(0)


####
# Start of project 1 (1:46:09)