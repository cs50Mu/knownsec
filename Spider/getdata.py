#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

import sqlite3

conn = sqlite3.connect('urls.db')
c = conn.cursor()

results = c.execute('select * from urls')

for keyword, title, content in results:
    try:
        with open('data/%s+%s.html' %(keyword, title),'w') as f:
            f.write(content)
    except:
        pass
