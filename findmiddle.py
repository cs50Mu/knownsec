#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""docstring
"""

__revision__ = '0.1'


def findMiddle(lst):   # 寻找平衡点
    for i in xrange(1, len(lst)-1):
        if sum(lst[:i]) == sum(lst[i+1:]):
            print i

a = [1,3,5,7,8,25,4,20]
b = [3,3,1,2,3]

def findMiddle2(lst):
    totle = sum(lst)

    add = 0
    for i in xrange(0, len(lst)-1):
        add += lst[i]
        if totle - lst[i+1] == 2 * add:
            print i+1, lst[i+1]

def findDomain(lst):  # 寻找支配点
    count = [ i for i,x in enumerate(lst) if lst.count(x) > len(lst)//2 ]  # elegant solution
    if count:
        print lst[count[0]], count

findDomain(b)
