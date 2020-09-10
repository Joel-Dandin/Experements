import cv2
import time
import numpy as np

car_classifier = cv2.CascadeClassifier('haarcascade_car.xml')

cap = cv2.VideoCapture('car_mov.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_classifier.detectMultiScale(grey,1.4,2)

    for(x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.imshow('Cars',Frame)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
