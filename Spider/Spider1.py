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

queue = deque()

visited = set()

conn = sqlite3.connect('urls.db')
c = conn.cursor()
c.execute('''CREATE TABLE urls
        (keyword text, title text, content text)''')

url_re = re.compile(r'href=\"(.+?)\"')
title_re = re.compile(r'<title>(.*)</title>')

crawDepth = 1

currentDepth = 0

start_url = 'http://news.dbanotes.net/', currentDepth

keyword = ['Python','python']

timeout = 3

queue.appendleft(start_url)
visited |= {start_url}

def db_insert(conn, keyword, title, content):
    c = conn.cursor()
    c.execute('insert into urls values (?,?,?)', (keyword, title, content))
    conn.commit()

while queue:
    url, currentDepth = queue.pop()
    try:
        r = requests.get(url, timeout=timeout)
        if 'html' not in r.headers['content-type']:
            continue
        print('Crawing %s, depth %d, %d left in queue' %(url, currentDepth, len(queue)))
        for key in keyword:
            if key in r.text:
                title = title_re.findall(r.text)[0]
                db_insert(conn, key, title, r.text)
        if currentDepth == crawDepth:  # 只爬指定的深度，当前深度还是要爬的，后面的就不继续爬了
            continue
        url_list = url_re.findall(r.text)
        if url_list:
            for url in url_list:
                if 'http' in url and url not in visited:
                    visited |= {url}
                    url = url, currentDepth + 1
                    queue.appendleft(url)
                    print('Adding url %s' %url[0])
    except:
        continue
conn.close()

