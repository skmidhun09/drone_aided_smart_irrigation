# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 11:48:52 2022

@author: dougl
"""

import cv2
import numpy as np
from djitellopy import tello
import time




def findFace(img):
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default')
    #img = cv2.imread('zero.jpg')
    cv2.imshow("Out", img)
    #imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Output", imgGray)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)
    myFaceListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cx = x + w // 2
        cy = y + h // 2
        Area = w * h
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        myFaceListC.append([cx, cy])
        myFaceListArea.append(Area)
        if len(myFaceListArea) != 0:
            i = myFaceListArea.index(max(myFaceListArea))
            return img, [myFaceListC[i], myFaceListArea[i]]
        else:
            return img, [[0, 0], 0]


def trackFace(info, w, pid, pError):
    Area = info[1]
    x, y = info[0]
    fb = 0
    error = x - w // 2
    speed = pid[0] * error + pid[1] * (error - pError)
    speed = int(np.clip(speed, -100, 100))

    if Area > fbRange[0] and Area < fbRange[1]:
        fb = 0
    elif Area > fbRange[1]:
        fb = -20
    elif Area < fbRange[0] and Area != 0:
        fb = 20
    if x == 0:
        speed = 0
        error = 0
        # print(speed, fb)

    # me.send_rc_control(0, fb, 0, speed)
    return error


# cap = cv2.VideoCapture (0)

me = tello.Tello()
me.connect()
print("Battery: ", me.get_battery(),"%")

me.takeoff()
me.streamon()
me.send_rc_control(0, 0, 10, 0)
time.sleep(2.2)

w, h = 360, 240
fbRange = [6200, 6800]
pid = [0.4, 0.4, 0]
pError = 0


while True:
    # _, img = cap.read()
    time.sleep(2)
    img = me.get_frame_read().frame
    img = cv2.resize(img, (w, h))
    img, info = findFace(img)
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break
