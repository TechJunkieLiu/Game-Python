# -*- coding: utf-8 -*-
__author__ = '刘志奇'
"""
 猜数游戏
"""

import random

# 创建随机数
num = random.randrange(1, 100)
# 获取输入
guess = int(input("输入任意数值: "))

while num != guess:  # 判断是否正确
    # 小于
    if guess < num:
        print("太小了")
        guess = int(input("再次输入数值: "))
    # 大于
    elif guess > num:
        print("太大了!")
        guess = int(input("再次输入数值: "))
    else:
        break
print("真棒，你猜对了!!")