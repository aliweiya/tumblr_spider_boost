# coding=utf-8
# Created by: dong4j.
# Date: 2016-12-10.
# Time: 00:20.
# Description:

import requests
import urllib
from bs4 import BeautifulSoup
import os
import traceback

def analysis(url_file, url):
    source_list = []
    # to get the source to second analysis
    try:
        second_res = requests.get(url)
    except:
        f = open("/home/ubuntu/log.txt", 'a')
        traceback.print_exc(file = f)
        f.flush()
        f.close()

    second_soup = BeautifulSoup(second_res.text, "html.parser")
    # get all <source> label
    second_source = second_soup.find_all("source")
    # get 'src' source
    for src in second_source:
        real_url = src.get('src', '').strip()
        print real_url
        source_list.append(real_url)
        url_file.writelines(real_url + '\n')

def get_url_from_file(file_path):
    all_url_count = 0
    url_file = open('url.txt', 'a+')
    htmlfile = open(file_path, 'r')
    for line in htmlfile:
        print line
        all_url_count += 1
        analysis(url_file, line)
    url_file.close()
    htmlfile.close()
    print '总文件数 =', all_url_count
    return None

if __name__ == '__main__':
    file_path = '/Users/codeai/Desktop/source.txt'
    get_url_from_file(file_path)
