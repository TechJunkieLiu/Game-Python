# -*- coding: utf-8 -*-
__author__ = '刘志奇'
"""
 数据爬取 txt
    获取header和cookie
    获取网页
    解析网页
    爬取内容
    数据存储
    清洗数据
"""

import requests
from bs4 import BeautifulSoup

# 获取 header 和 cookie
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'cookie': '__yjs_duid=1_b1ac9fc87dce4de5552d7cf0924fb4981686228951567; u=b0281776fd75d3eefeb3562b2a5e6534; __bid_n=1889b14047a51b2b754207; FPTOKEN=qU+ieOMqkW6y6DlsOZ+D/T+SCY6yS3dYvGXKibFoGBijKuUuSbc3ACFDzjlcC18wuDjNLENrw4ktAFAqnl3Akg492Lr4fbvNrkdJ/ZQrluIdklkNDAKYnPrpcbe2H9y7AtX+/b+FCTkSTNv5+qB3OtQQ3BXXsEen72oEoAfK+H6/u6ltZPdyHttJBJiXEDDS3EiUVt+S2w+8ozXENWbNt/AHeCgNUMmdeDinAKCR+nQSGK/twOoTLOU/nxBeSAazg+wu5K8ooRmW00Bk6XAqC4Cb829XR3UinZHRsJxt7q9biKzYQh+Yu5s6EHypKwpA6RPtVAC1axxbxza0l5LJ5hX8IxJXDaQ6srFoEzQ92jM0rmDynp+gT+3qNfEtB2PjkURvmRghGUn8wOcUUKPOqg==|mfg5DyAulnBuIm/fNO5JCrEm9g5yXrV1etiaV0jqQEw=|10|dcfdbf664758c47995de31b90def5ca5; PHPSESSID=18397defd82b1b3ef009662dc77fe210; Hm_lvt_de3f6fd28ec4ac19170f18e2a8777593=1686322028,1686360205; history=cid%3A2455%2Ccid%3A2476%2Ccid%3A5474%2Ccid%3A5475%2Ccid%3A2814%2Cbid%3A3667; Hm_lpvt_de3f6fd28ec4ac19170f18e2a8777593=1686360427'
}

# 获取网页
response = requests.get('https://www.maigoo.com/news/484526.html', headers=header)

# 解析网页
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)

# 爬取内容
content = "#modellist-1046834 > div > div > div.mod_desc.fcolor30.font14.line2em.tleft > p"
print(content)

# 数据存储
fo = open("./重庆市渝中区中华路小学.txt", 'a', encoding="utf-8")

# 清洗数据
a = soup.select(content)
for i in range(0, len(a)):
    a[i] = a[i].text
    fo.write(a[i] + '\n')
    fo.close()