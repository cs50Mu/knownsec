#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""方法一是我自己捣鼓的
方法二是我在CodeForces上看到了，效果应该是一样的
都是为了在转换26的倍数的时候能够得出正确的结果，
做出的一点特殊处理，不过显然后者更加优雅
"""

__revision__ = '0.1'

import sys

def numTochar(num):
    result = ''
    ori = num
    while num:
        mod = num % 26
        if mod == 0:
            mod = 26
            num = num/26 - 1 # special cases for 'Z' 
        else:
            num /= 26
        result = chr(mod + ord('A') - 1) + result
    return result,ori

def numTochar2(num):
    result = ''
    ori = num
    while num:
        mod = num % 26
        if mod == 0:
            mod = 26
        num -= 1       # a more elegant solution
        num /= 26
        result = chr(mod + ord('A') - 1) + result
    return result,ori

print numTochar(int(sys.argv[1]))
#for i in xrange(1,59):
#    print numTochar(i)

