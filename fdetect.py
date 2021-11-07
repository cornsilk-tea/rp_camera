## Face Detecteion Code

import numpy as np
import cv2
import time
from pathlib import Path
# from picamera import PiCamera
from time import sleep
font = cv2.FONT_HERSHEY_DUPLEX

def FaceDetect():
    
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')

    try:
        cam = cv2.VideoCapture(0)
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cam.set(cv2.CAP_PROP_FPS, 20)
    except:
        print("Camera Loading Error!!")
        return

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        height, width, channel = frame.shape
        img90 = cv2.getRotationMatrix2D((width/2, height/2), -90, 1)
        img_res = cv2.warpAffine(frame, img90, (width, height))
        
        gray_base = cv2.cvtColor(img_res, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray_base)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize = (10, 10),
        )
        if len(faces) >=2:
            print(len(faces))

        cv2.putText(img_res, "Finding Faces.." , (5,15), font, 0.7, (255, 255, 255), 1)

        for (x, y, w, h) in faces:
            cv2.rectangle(img_res, (x, y), (x+w, y+h), (255, 0, 0), 2) 
            cv2.putText(img_res, "Detected Face", (x-5, y-5), font, 0.5, (255, 255, 0), 2)
            exrect = img_res[y-int(h/100):y + h + int(h/100), x - int(w/100):x + w + int(w/100)]
            cv2.imshow("Detected Face", img_res)

            cnt_time = 10
            while cnt_time > 0:
                cnt = "{}".format(str(cnt_time))
                cv2.putText(img_res, cnt, (10, 50), font, 1.0, (0, 0, 0), 2)
                cnt_time = cnt_time-1

            cv2.imwrite('./exface.jpg', img_res)

            if cv2.waitKey(33) > 0:
                break

    cam.release()
    cv2.destroyAllWindows()

FaceDetect()
