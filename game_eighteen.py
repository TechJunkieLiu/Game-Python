# -*- coding: utf-8 -*-
__author__ = '刘志奇'
"""
 OpenCV 人脸检测（暂无训练模型）
"""

import cv2

face_cascade = cv2.CascadeClassifier('face_detector.xml')
img = cv2.imread('D:\picture\images\person.jpg')
faces = face_cascade.detectMultiScale(img, 1.1, 10)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
cv2.imwrite("D:\picture\images\person_.jpg", img)
print('Successfully saved')
