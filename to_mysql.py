# -*- coding:utf-8 -*-
import signal
import sys
import requests
import threading
import Queue
import time
import re
import traceback
import MySQLdb
from bs4 import BeautifulSoup

mutex = threading.Lock()
is_exit = False


class Tumblr(threading.Thread):

    def __init__(self, queue):
        self.user_queue = queue
        # saved user list
        self.total_user = []
        # saved url list
        self.total_url = []
        self.f_user = open('user_to_mysql.txt', 'a+')
        self.f_source = open('source_to_mysql.txt', 'a+')
        self.f_img = open('img_to_mysql.txt', 'a+')
        # 第一次的 video_url
        self.video_url = ''
        self.second_video_url = ''
        self.db = MySQLdb.connect("localhost", "root", "bVWrFXDqfhKV*xRMzsag8BGb", "spider")

        threading.Thread.__init__(self)

    def download(self, url):
        # url   http://zzzzzxxxbbb.tumblr.com
        try:
            res = requests.get(url)
            img_list = []
            source_list = []
            tmp_img = []
            tmp_source = []
            soup = BeautifulSoup(res.text)
            # get all <iframe> label
            iframes = soup.find_all('iframe')
            # foreach url
            for i in iframes:
                # get 'src' source in  iframe  https://www.tumblr.com/video/zzzzzxxxbbb/154210927087/700/
                source = i.get('src', '').strip()
                # if 'https://www.tumblr.com/video' string in source and not in saved url list
                if source and source.find('https://www.tumblr.com/video') != -1 and source not in self.total_url:
                    source_list.append(source)
                    tmp_source.append(source)
                    print 'new link:' + source
                    video_url = source
                    # to get the source to second analysis
                    second_res = requests.get(source)
                    second_soup = BeautifulSoup(second_res.text)
                    # get all <source> label
                    second_source = second_soup.find_all("source")
                    # get 'src' source
                    for src in second_source:
                        real_url = src.get('src', '').strip()
                        print real_url
                        second_video_url = real_url
                        source_list.append(real_url)
                        tmp_source.append(real_url)
                        # 插入数据库
                        # 执行sql语句
                        self.db.cursor().execute(
                            "insert into t_video (user_id, url, down_rul, title, liked, user_name) values('%d','%s','%s','%s','%d','%s')" % (
                                1, video_url, second_video_url, 'xxx', 100, self.user_queue.get()))
                        # 提交到数据库执行
                        self.db.commit()
                        # try:
                        #     # 执行sql语句
                        #     self.db.cursor.execute(
                        #         "insert into t_video (user_id, url, down_rul, title, liked, user_name) values('%d','%s','%s','%s','%d','%s')" % (
                        #         1, video_url, second_video_url, 'xxx', 100, self.user_queue.get()))
                        #     # 提交到数据库执行
                        #     self.db.commit()
                        # except:
                        #     # Rollback in case there is any error
                        #     self.db.rollback()

                # analysis image
                # 正则搜索出 username
                # res = 'http://zzzzzxxxbbb.tumblr.com'
                # reg = r'^http:\/\/([a-z0-9]+)'
                # url_re = re.search(reg, url, re.M | re.I)
                # if url_re:
                #     username = url_re.group(1)
                #     if source and source.find('http://' + username + '.tumblr.com/post/') != -1:
                #         print source
                #         img_res = requests.get(source)
                #         img_soup = BeautifulSoup(img_res.text)
                #         img_source = img_soup.find_all("img")
                #         for img in img_source:
                #             img_url = img.get('src', '').strip()
                #             print img_url
                #             img_list.append(img_url)
                #             tmp_img.append(img_url)

            tmp_user = []
            # get user
            new_users = soup.find_all(class_ = 'reblog-link')
            # foreach relationship user
            for user in new_users:
                username = user.text.strip()
                if username and username not in self.total_user:
                    self.user_queue.put(username)
                    self.total_user.append(username)
                    tmp_user.append(username)
                    print 'new user:' + username

            mutex.acquire()
            if tmp_user:
                self.f_user.write('\n'.join(tmp_user) + '\n')
            if tmp_source:
                self.f_source.write('\n'.join(tmp_source) + '\n')
            # if tmp_img:
            #     self.f_img.write('\n'.join(tmp_img) + '\n')
            mutex.release()
        except:
            f = open("/Users/codeai/Desktop/log.txt", 'a')
            traceback.print_exc(file = f)
            f.flush()
            f.close()

    def run(self):
        global is_exit
        while not is_exit:
            user = self.user_queue.get()
            url = 'http://%s.tumblr.com/' % user
            self.download(url)
            time.sleep(2)
        self.f_user.close()
        self.f_source.close()
        self.f_img.close()


def handler(signum, frame):
    global is_exit
    is_exit = True
    print "receive a signal %d, is_exit = %d" % (signum, is_exit)
    sys.exit(0)


def main():

    if len(sys.argv) < 2:
        print 'usage: python tumblr.py username'
        sys.exit()
    username = sys.argv[1]

    NUM_WORKERS = 10
    queue = Queue.Queue()
    # modify username
    queue.put(username)

    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGTERM, handler)

    threads = []
    for i in range(NUM_WORKERS):
        tumblr = Tumblr(queue)
        tumblr.setDaemon(True)
        tumblr.start()
        threads.append(tumblr)

    while True:
        for i in threads:
            if not i.isAlive():
                break
        time.sleep(1)


if __name__ == '__main__':
    main()
