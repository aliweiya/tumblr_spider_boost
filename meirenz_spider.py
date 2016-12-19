# coding=utf-8
# Created by: dong4j.
# Date: 2016-12-10.
# Time: 21:22.
# Description: 

import signal
import sys
import requests
import threading
import Queue
import time
import re
import traceback
from bs4 import BeautifulSoup

def spider():
    i = 1
    root_url = 'http://tuigirlvip.com/node/show/2/' + str()
    res = requests.get(root_url)
    print res.text
    soup = BeautifulSoup(res.text,"html.parser")

if __name__ == '__main__':
    spider()