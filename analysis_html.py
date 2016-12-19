# coding=utf-8
# Created by: dong4j.
# Date: 2016-12-10.
# Time: 00:20.
# Description:
import traceback

import requests
import urllib
from bs4 import BeautifulSoup
import os

# 解析获取到的 html
def analysis(url_file, url):
    source_list = []
    # to get the source to second analysis
    try:
        second_res = requests.get(url)
        second_soup = BeautifulSoup(second_res.text, "html.parser")
        # get all <source> label
        second_source = second_soup.find_all("source")
        # get 'src' source
        for src in second_source:
            real_url = src.get('src', '').strip()
            print real_url
            source_list.append(real_url)
            url_file.writelines(real_url + '\n')
    except:
        f = open("/home/ubuntu/log.txt", 'a')
        traceback.print_exc(file = f)
        f.flush()
        f.close()


def get_url_from_file(file_path):
    # 新建一个文件,用来保存解析后的 url
    all_url_count = 0
    url_file = open('url.txt', 'a+')
    # 以只读的方式打开本地html文件
    htmlfile = open(file_path, 'r')
    for line in htmlfile:
        if line != '':
            print line
            all_url_count += 1
            analysis(url_file, line)
            line = ''

    url_file.close()

    # htmlpage = htmlfile.read()
    # # print htmlpage
    # # 实例化一个BeautifulSoup对象
    # soup = BeautifulSoup(htmlpage, "html.parser")
    # print soup.title.string  # 打印该html的标题
    # # 连接目录与文件名或目录（目录，文件夹名或目录），此处以html标题命名文件夹名字
    # filepath = os.path.join(localpath, soup.title.string)
    # # 判断，若该文件路径不存在，则创建该目录（mkdirs创建多级目录，midir创建单级目录）
    # if not os.path.exists(filepath):
    #     os.makedirs(filepath)
    # # 查找所有标签值为img，属性class为BDE_Image的数据，返回一个集合list
    # cctag = soup.find_all('img', attrs = {'class': 'BDE_Image'})
    # for i in cctag:
    #     print i.attrs['src']
    #     # 保存下载每一组数据属性为src的内容（网页地址）到本地，名字为原图片名称：http://imgsrc.baidu.com/forum/w%3D580/sign=5b3aec8704f3d7ca0cf63f7ec21ebe3c/ad13728b4710b9120be45d47cbfdfc0392452260.jpg
    #     urllib.urlretrieve(i.attrs['src'], os.path.join(filepath, '%s' % i.attrs['src'].split('/')[-1]))
    htmlfile.close()
    print '总文件数 =', all_url_count
    return None



# 获取指定文件夹下的所有文件列表
# def print_path(level, path):
#     global allFileNum
#     '''''
#     打印一个目录下的所有文件夹和文件
#     '''
#     # 所有文件夹，第一个字段是次目录的级别
#     dirList = []
#     # 所有文件
#     fileList = []
#     # 返回一个列表，其中包含在目录条目的名称(google翻译)
#     files = os.listdir(path)
#     # 先添加目录级别
#     dirList.append(str(level))
#     for f in files:
#         if os.path.isdir(path + '/' + f):
#             # 排除隐藏文件夹。因为隐藏文件夹过多
#             if f[0] == '.':
#                 pass
#             else:
#                 # 添加非隐藏文件夹
#                 dirList.append(f)
#         if os.path.isfile(path + '/' + f):
#             # 添加文件
#             fileList.append(f)
#             # 当一个标志使用，文件夹列表第一个级别不打印
#     i_dl = 0
#     for dl in dirList:
#         if i_dl == 0:
#             i_dl += 1
#         else:
#             # 打印至控制台，不是第一个的目录
#             print '-' * (int(dirList[0])), dl
#             # 打印目录下的所有文件夹和文件，目录级别+1
#             print_path((int(dirList[0]) + 1), path + '/' + dl)
#     for fl in fileList:
#         # 打印文件
#         print '-' * (int(dirList[0])), fl
#         # 随便计算一下有多少个文件
#         allFileNum += 1

if __name__ == '__main__':
    # print_path(1, '/home/lizheng')
    file_path = '/Users/codeai/Desktop/source.txt'
    get_url_from_file(file_path)

