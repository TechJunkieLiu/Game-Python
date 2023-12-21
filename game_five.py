# -*- coding: utf-8 -*-
__author__ = '刘志奇'
"""
 二维码
"""

import pyqrcode

# 设置二维码信息
s = "https://www.aiyangniu.cn"

# 生成二维码
url = pyqrcode.create(s)

# 保存二维码
url.svg("aiyangniu.svg", scale=10)