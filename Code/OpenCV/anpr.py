import cv2

car_cascade_path = "Resources/Cascades/cars.xml"
car_path = "Resources/lambo.png"

carCascade = cv2.CascadeClassifier(car_cascade_path)

img = cv2.imread(car_path)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = carCascade.detectMultiScale(imgGray, 1.1, 1)

for (x, y, w, h) in faces:

    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 

cv2.imshow("car", img)
cv2.waitKey(0)