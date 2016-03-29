#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""中文转成utf8编码后就可以搜索了，这是对Python2来说的
Python3不需要，直接用就可以了
"""

__revision__ = '0.1'

import re
import requests
from collections import deque
import sqlite3
import threading
import os
import time

#queue = deque()
#
#visited = set()

#conn = sqlite3.connect('urls.db')
#c = conn.cursor()
#c.execute('''CREATE TABLE urls
#        (keyword text, title text, content text)''')
#
#url_re = re.compile(r'href=\"(.+?)\"')
#title_re = re.compile(r'<title>(.*)</title>')
#
#crawDepth = 3
##
##currentDepth = 0
##
#start_url = 'http://www.163.com', 0
#
#keyword = ['Python','python']
#
#timeout = 3

#queue.appendleft(start_url)
#visited |= {start_url}

def db_insert(conn, keyword, title, content):
    c = conn.cursor()
    c.execute('insert into urls values (?,?,?)', (keyword, title, content))
    conn.commit()

#while queue:
#    url, currentDepth = queue.pop()
#    try:
#        r = requests.get(url, timeout=timeout)
#        if 'html' not in r.headers['content-type']:
#            continue
#        print('Crawing %s, depth %d, %d left in queue' %(url, currentDepth, len(queue)))
#        for key in keyword:
#            if key in r.text:
#                title = title_re.findall(r.text)[0]
#                db_insert(conn, key, title, r.text)
#        if currentDepth == crawDepth:  # 只爬指定的深度，当前深度还是要爬的，后面的就不继续爬了
#            continue
#        url_list = url_re.findall(r.text)
#        if url_list:
#            for url in url_list:
#                if 'http' in url and url not in visited:
#                    visited |= {url}
#                    url = url, currentDepth + 1
#                    queue.appendleft(url)
#                    print('Adding url %s' %url[0])
#    except:
#        continue
#conn.close()


def Spider(task_queue, visited_queue):
    conn = sqlite3.connect('urls.db')
    url, currentDepth = task_queue.pop()
    try:
        r = requests.get(url, timeout=timeout)
        if 'html' not in r.headers['content-type']:
            return
        print('Crawing %s, depth %d, %d left in queue' %(url, currentDepth, len(task_queue)))
        for key in keyword:
            if key in r.text:
                title = title_re.findall(r.text)[0]
                db_insert(conn, key, title, r.text)
        if currentDepth == crawDepth:  # 只爬指定的深度，当前深度还是要爬的，后面的就不继续爬了
            return
        url_list = url_re.findall(r.text)
        if url_list:
            for url in url_list:
                if 'http' in url and url not in visited_queue:
                    visited_queue.append(url)
                    url = url, currentDepth + 1
                    task_queue.appendleft(url)
                    print('Adding url %s' %url[0])
    except:
        pass


class Worker(threading.Thread):
    def __init__(self, work, visited_queue, task_queue):
        super(Worker, self).__init__()
        self.task_queue = task_queue
        self.work = work
        self.visited_queue = visited_queue

    def run(self):
        while True:
            try:
                self.work(self.task_queue, self.visited_queue)
            except:
                print('zhongmele')
                break
class PoolManager():
    def __init__(self, work, visited_queue, task_queue, thread_num = 2):
        self.thread_num = thread_num
        self.visited_queue = visited_queue
        self.task_queue = task_queue
        self.work = work
        self.threads = []

    def add_task(self, url):
        task_queue.appendleft(url)

    def start(self):
        for i in range(self.thread_num):
            w = Worker(self.work, self.visited_queue, self.task_queue)
            w.setDaemon(True)
            w.start()
            self.threads.append(w)

    def wait_all(self):
        for w in self.threads:
            w.join()

if __name__ == "__main__":
    os.remove('urls.db')
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE urls
            (keyword text, title text, content text)''')

    url_re = re.compile(r'href=\"(.+?)\"')
    title_re = re.compile(r'<title>(.*)</title>')

    crawDepth = 3

    start_url = 'http://www.ibm.com/developerworks/cn/topics/', 0

    keyword = ['Python']

    timeout = 3

    task_queue = deque()
    visited_queue = deque()
    t1 = time.time()
    task_queue.appendleft(start_url)
    Spider(task_queue, visited_queue)  # 先给任务池里加点任务，否则任务不足后面的线程会直接退出
    pool = PoolManager(Spider, visited_queue, task_queue, thread_num = 60)
    pool.start()
    pool.wait_all()
    t2 = time.time()
    print('共计用时%d秒' %(t2 - t1))
