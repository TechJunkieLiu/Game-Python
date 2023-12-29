# -*- coding: utf-8 -*-
__author__ = '刘志奇'

import cv2
import numpy as np

"""
 读取图片并展示
"""
image1 = cv2.imread(r"D:/picture/1.jpg")
cv2.imshow("image1", image1)
cv2.waitKey(0)

"""
 读取图片并保存（黑白色）
"""
image2 = cv2.imread(r"D:/picture/1.jpg", 0)
cv2.imwrite(r"D:/picture/10.jpg", image2)

"""
 图片缩放
"""
image3 = cv2.imread(r"D:/picture/1.jpg")
print(image3.shape)
# 获取图片的高度和宽度
height, width = image3.shape[:2]
image4 = cv2.resize(image3, (int(0.5 * width), int(0.5 * height)))
print(image4.shape)  #
cv2.imwrite(r"D:/picture/11.jpg", image4)

"""
 图片翻转
"""
image5 = cv2.imread(r"D:/picture/1.jpg")
# 0垂直翻转 ；1水平翻转 ；-1水平和垂直翻转
imgFlip1 = cv2.flip(image5, -1)
cv2.imshow("image5", imgFlip1)
cv2.waitKey(0)

"""
 图片旋转90°
"""
image6 = cv2.imread(r"D:/picture/1.jpg")
# 顺时针旋转90度
image7 = cv2.rotate(image6, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("image7", image7)
cv2.waitKey(0)

"""
 图片旋转任意角度(法一)
"""
# 第一个参数穿opencv读取的图像，第二个参数传入需要旋转的角度
def rotate_bound(image, angle):
    # 取前两个值（H，W）
    height, width = image.shape[:2]
    # 第一个参数旋转中心，第二个参数旋转角度，第三个参数缩放比例
    # 以图像中心为旋转中心
    center = (width // 2, height // 2)
    # 等比例旋转，即旋转后尺度不变
    scale = 1
    # 获得旋转矩阵
    M = cv2.getRotationMatrix2D(center, -angle, scale)

    # 进行仿射变换，其中
    # “,borderValue=(255,255,255)”定义边界填充色彩白色，省略默认黑色,相当于borderValue=(0,0,0)
    return cv2.warpAffine(image, M, (width, height), borderValue=(255, 255, 255))


image8 = cv2.imread(r"D:/picture/1.jpg")
image9 = rotate_bound(image8, 45)
cv2.imshow('image', image9)  # 显示图片
cv2.waitKey(0)

"""
 图片旋转任意角度(法二)
"""
# 第一个参数穿opencv读取的图像，第二个参数传入需要旋转的角度
def rotate_bound(image, angle):
    # 获取图像的尺寸，并确定中心
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # 获取旋转矩阵（应用角度的负数以顺时针旋转）
    # 获取正弦和余弦（即矩阵的旋转分量）
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # 计算图像的新边界尺寸
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # 调整矩阵
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # 进行仿射变换，其中
    # “,borderValue=(255,255,255)”定义边界填充色彩白色，省略默认黑色,相当于borderValue=(0,0,0)
    return cv2.warpAffine(image, M, (nW, nH), borderValue=(255, 255, 255))
image10 = cv2.imread(r"D:/picture/1.jpg")
image11 = rotate_bound(image10, 45)
cv2.imshow('image', image11)  # 显示图片
cv2.waitKey(0)

"""
 图片旋转任意角度(法三)
"""
def opencv_rotate(img, angle):
    h, w = img.shape[:2]  # 图像的（行数，列数，色彩通道数）
    center = (w / 2, h / 2)
    scale = 1.0
    # 1 获取M矩阵
    # cv2.getRotationMatrix2D(获得仿射变化矩阵)
    M = cv2.getRotationMatrix2D(center, -angle, scale)
    # 2 扩大画布，新的宽高，radians(angle) 把角度转为弧度 sin(弧度)
    new_H = int(w * np.fabs(np.sin(np.radians(angle))) + h * np.fabs(np.cos(np.radians(angle))))
    new_W = int(h * np.fabs(np.sin(np.radians(angle))) + w * np.fabs(np.cos(np.radians(angle))))
    # 3 平移
    M[0, 2] += (new_W - w) / 2
    M[1, 2] += (new_H - h) / 2

    # cv2.warpAffine(进行仿射变化)
    rotate = cv2.warpAffine(img, M, (new_W, new_H), borderValue=(0, 0, 0))
    return rotate
image12 = cv2.imread(r"D:/picture/1.jpg")
image13 = opencv_rotate(image12, 45)
cv2.imshow('image', image13)  # 显示图片
cv2.waitKey(0)
