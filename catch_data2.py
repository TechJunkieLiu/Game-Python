# -*- coding: utf-8 -*-
__author__ = '刘志奇'
"""
 数据爬取 excel
    获取header和cookie
    获取网页
    解析网页
    爬取内容
    数据存储
    清洗数据
"""

import os
import time
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 创建Excel文件
wb = Workbook()
ws = wb.active

# 爬取地址url
url = 'https://www.maigoo.com/news/484526.html'

# 请求头
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'cookie': '__yjs_duid=1_b1ac9fc87dce4de5552d7cf0924fb4981686228951567; u=b0281776fd75d3eefeb3562b2a5e6534; __bid_n=1889b14047a51b2b754207; FPTOKEN=qU+ieOMqkW6y6DlsOZ+D/T+SCY6yS3dYvGXKibFoGBijKuUuSbc3ACFDzjlcC18wuDjNLENrw4ktAFAqnl3Akg492Lr4fbvNrkdJ/ZQrluIdklkNDAKYnPrpcbe2H9y7AtX+/b+FCTkSTNv5+qB3OtQQ3BXXsEen72oEoAfK+H6/u6ltZPdyHttJBJiXEDDS3EiUVt+S2w+8ozXENWbNt/AHeCgNUMmdeDinAKCR+nQSGK/twOoTLOU/nxBeSAazg+wu5K8ooRmW00Bk6XAqC4Cb829XR3UinZHRsJxt7q9biKzYQh+Yu5s6EHypKwpA6RPtVAC1axxbxza0l5LJ5hX8IxJXDaQ6srFoEzQ92jM0rmDynp+gT+3qNfEtB2PjkURvmRghGUn8wOcUUKPOqg==|mfg5DyAulnBuIm/fNO5JCrEm9g5yXrV1etiaV0jqQEw=|10|dcfdbf664758c47995de31b90def5ca5; PHPSESSID=18397defd82b1b3ef009662dc77fe210; Hm_lvt_de3f6fd28ec4ac19170f18e2a8777593=1686322028,1686360205; history=cid%3A2455%2Ccid%3A2476%2Ccid%3A5474%2Ccid%3A5475%2Ccid%3A2814%2Cbid%3A3667; Hm_lpvt_de3f6fd28ec4ac19170f18e2a8777593=1686360427'
}
response = requests.get(url, headers=header)
time.sleep(0.01)
print(response)

# 获取网页信息
#soup = BeautifulSoup(response.content, 'lxml')
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)

# 解析网页数据
# tr_tags = soup.find('div', class_="md_1009 modelbox tcenter").get_text()
tr_tags = soup.find_all('div', class_="md_1009 modelbox tcenter")
print(tr_tags)

# 循环遍历获取tr标签下的td标签文本
td_tags = soup.select('tr td')

for i in range(0, len(td_tags), 2):
    school_name = td_tags[i].get_text()
    address = td_tags[i + 1].get_text()
    # score = td_tags[i + 2].get_text()
    time.sleep(0.1)
    print(f'正在爬取：--{school_name}--{address}--')
    # 将数据项转换为一个元组
    row = (school_name, address)
    # 将数据行写入Excel表格
    ws.append(row)
    # 将文件保存到桌面
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "重庆市小学爬取.xlsx")
    wb.save(file_path)
    print('数据爬取完成！')