from cv2 import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

faceCascade = cv2.CascadeClassifier("C:\\Users\\ETG30\\OneDrive\\Desktop\\Python\\OpenCV\\Resources\\haarcascade_frontalface_default.xml")

while True:

    success, img = cap.read()

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        print(f"Face loacted at ({x},{y}),({x+w},{y+h})")
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.line(img,(x+w,y),(x+w+30,y-h+100),(255,0,0),2)
        cv2.rectangle(img,(x+w+30,y-h+100),(x+w+105,y-h+70),(255,255,255),cv2.FILLED)
        cv2.rectangle(img,(x+w+30,y-h+100),(x+w+105,y-h+70),(255,0,0),2)
        cv2.putText(img,"Face",(x+w+31,y-h+96),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)

    cv2.imshow("webcam 0", img)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break