#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 2014/09/18

"""第一个实现是我自己想的，比较ugly
第三个实现是我在一站式学习C编程上看到的，
第二个实现是我根据第三个的思想用递归重写的
"""

__revision__ = '0.1'

#import pdb
#pdb.set_trace()

import random

def binarySearch(lst, element, start, end):
    mid = (start + end)/2 
    if element == lst[mid]:
        print 'Found, %d' % mid
    elif mid == start:
        if element == lst[mid+1]:  # 主要处理两个相邻的数的情况，这种情形下mid必然等于start
            print 'Found, %d' % (mid+1) # 因此如果end（也就是mid+1）不等于element的话，则没找到
        else:
            print 'Not found'
    elif element > lst[mid]:
        return binarySearch(lst, element, mid, end)
    elif element < lst[mid]:
        return binarySearch(lst, element, start, mid)

def binarySearch2(lst, element, start, end):
    mid = (start + end)/2
    if element == lst[mid]:
        return 'Found, %d' % mid
    elif start > end:
        return 'Not found'
    elif element < lst[mid]:
        return binarySearch2(lst, element, start, mid-1)
    elif element > lst[mid]:
        return binarySearch2(lst, element, mid+1, end)

def binarySearch3(lst, element):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end)/2
        if lst[mid] == element:
            return 'Found', mid
        elif lst[mid] > element:
            end = mid - 1
        elif lst[mid] < element:
            start = mid + 1
    return 'Not found'

lst = [ random.randint(1, 10000) for _ in xrange(10) ]
lst = list(set(lst))
lst.sort()
print lst

for i in lst:
    print binarySearch2(lst, i, 0, len(lst)-1)
#binarySearch2(lst, 99, 0, len(lst)-1)
#binarySearch3(lst, 99)
#for i in lst:
#    print binarySearch3(lst, i)
