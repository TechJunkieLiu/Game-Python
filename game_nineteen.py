# -*- coding: utf-8 -*-
__author__ = '刘志奇'
"""
 OpenCV 图像转铅笔素描
"""

import cv2

image = cv2.imread("D:\picture\images\\narendra_modi.jpg")
cv2.imshow("Man", image)
cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.waitKey(0)

inverted_image = 255 - gray_image
cv2.waitKey()

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)

cv2.imwrite("D:\picture\images\\narendra_modi_.jpg", pencil_sketch)
cv2.waitKey(0)
