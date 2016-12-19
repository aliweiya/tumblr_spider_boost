# coding=utf-8
# Created by: dong4j.
# Date: 2016-12-10.
# Time: 02:03.
# Description: 

import traceback
import requests
import urllib
import re
from bs4 import BeautifulSoup
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 解析获取到的 html
def analysis(usernamea, url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    iframes = soup.find_all('iframe')
    reg = r'^http:\/\/([a-z0-9]+)'
    url_re = re.search(reg, url, re.M | re.I)
    if url_re:
        username = url_re.group(1)
        for i in iframes:
            source = i.get('src', '').strip()
            # 解析图片
            if source and source.find('http://'+username+'.tumblr.com/post/') != -1:
                print source
                second_res = requests.get(source)
                second_soup = BeautifulSoup(second_res.text)
                second_source = second_soup.find_all("img")
                for src in second_source:
                    real_url = src.get('src', '').strip()
                    print real_url

if __name__ == '__main__':
    analysis('zzzzzxxxbbb', 'http://zzzzzxxxbbb.tumblr.com')
