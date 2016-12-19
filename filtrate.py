# coding=utf-8
# Created by: dong4j.
# Date: 2016-12-10.
# Time: 04:29.
# Description: 从文件中过滤到长度不对的 url

# https://www.tumblr.com/video_file/t:QFz7xF5t9dkWYzL5MQyciw/154170000726/tumblr_nx8ra5JVx21ujgbss

def filter_url():
    # ss = 'https://www.tumblr.com/video_file/t:QFz7xF5t9dkWYzL5MQyciw/154170140996/tumblr_ohtvt0q4Uj1uu6lvt/480'
    # print ss[:96]
    new_url = ''
    urls = open("/Users/codeai/Desktop/url.txt", "r")
    new_urls = open("/Users/codeai/Desktop/new_urls.txt", "a+")
    for url in urls:
        if url != '':
            # print len(url)
            # # 为真时的结果 if 判断条件 else 为假时的结果（注意，没有冒号）
            # new_url = url[:96] if len(url) == 101 else (url if len(url) == 97 else "")
            # if len(new_url) != 0:
            #     new_urls.writelines(new_url)
            if len(url) == 101:
                new_url = url[:96] + '\n'
            elif len(url) == 97:
                new_url = url
            else:
                new_url = ''
            new_urls.writelines(new_url)
    urls.close()
    new_urls.close()

if __name__ == '__main__':
    filter_url()
