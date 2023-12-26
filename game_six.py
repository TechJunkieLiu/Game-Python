# -*- coding: utf-8 -*-
__author__ = '刘志奇'
"""
 语言检测
"""

from langdetect import detect

text = input("输入信息：")
print(detect(text))
