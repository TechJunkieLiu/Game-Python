# -*- coding: utf-8 -*-
from __future__ import with_statement

__author__ = '刘志奇'
"""
 URL缩短
"""

import contextlib

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib3 import urlopen
import sys


def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url': url}))
    # print(request_url)
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')


source_url = ('https://huaweicloud.csdn.net/637f7cd9dacf622b8df86131.html?spm=1001.2101.3001.6650.5&utm_medium'
              '=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Eactivity-5-125669955-blog-131492092.235'
              '%5Ev39%5Epc_relevant_default_base&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault'
              '%7ECTRLIST%7Eactivity-5-125669955-blog-131492092.235%5Ev39%5Epc_relevant_default_base'
              '&utm_relevant_index=8')


def main():
    for result_url in map(make_tiny, [source_url]):
        print('原始地址：' + source_url + '\n压缩地址：' + result_url)


if __name__ == '__main__':
    main()
