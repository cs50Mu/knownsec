#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

#def fib(n):
#    if n == 1 or n == 2:
#        return 1
#    return fib(n-1) + fib(n-2)
########## Memorized version ##########
d = {}

def fib2(n):
    if n in d:
        return d[n]
    else:
        if n == 1 or n == 2:
            return 1
        d[n] = fib2(n-1) + fib2(n-2)
        return d[n]
#######################################

############ using decorator ##########
def memorize(f):
    d = {}
    def wrapper(*args):
        if args in d:
            return d[args]
        else:
            d[args] = f(*args)
            return d[args]
    return wrapper

@memorize
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)
######################################
print fib(500)
