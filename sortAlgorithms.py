#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""各个排序算法都有自己的特点，不能单纯的说，
某个就是好，选择排序对于任何形式的输入，时间
复杂度都是N^2，而插入排序对于部分排好序的输入，
时间复杂度是线性的，归并排序对于任何形式的输入，
时间复杂度都是N*logN，所以要根据输入的特点来
选择最优的排序算法。
  还有一个问题是排序算法的稳定性，是指先按照某个
关键字排序后，再按照另一个关键字排序后，之前的
排序没有被当前的排序打乱，
  Python不支持类似i++的自增运算符
"""

__revision__ = '0.1'

import random
import time
import pdb



lst = [ random.randint(1,10000) for _ in xrange(10000) ]

def timeit(f):
    def wrapper(*args):
        t1 = time.time()
        result = f(*args)
        t2 = time.time()
        print 'time: %f' %(t2 - t1)
        return result
    return wrapper

@timeit
def selectionSort(lst):
    for i in xrange(len(lst)):
        minNum = lst[i]
        for j in xrange(i+1, len(lst)):
            if lst[j] < minNum:
                minNum = lst[j]
        lst[i], minNum = minNum, lst[i]
    return lst

@timeit
def insertionSort(lst):
    for i in xrange(1, len(lst)):
        for j in xrange(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else:          # 若已经满足条件，则后面的都不需要判断了，加上这个后shell排序效率大增
                break      # 但insertion sort效果不明显
    return lst

@timeit
def shellSort(lst):
    h = 1
    while (h < len(lst)/3):
        h = h * 3 + 1


    while (h >= 1):
        for i in xrange(h, len(lst)):
            for j in xrange(i, h-1, -h):  # 此处因为是倒着数的，所以应该为i到h-1，一开始写成h+1了。。
                if lst[j] < lst[j-h]:
                    lst[j], lst[j-h] = lst[j-h], lst[j]
                else:      # 若已经满足条件，则后面的都不需要判断了，加上这个后shell排序效率大增
                    break  # 快了75倍！
        h /= 3
    return lst

def merge(lst1, lst2):
    result = []
    while lst1 and lst2:
        if lst1[0] < lst2[0]:
            result.append(lst1.pop(0))
        else:
            result.append(lst2.pop(0))
    if lst1:
        result.extend(lst1)
    if lst2:
        result.extend(lst2)
    return result

def mergeSort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    first = mergeSort(lst[:mid])
    second = mergeSort(lst[mid:])
    return merge(first, second)

@timeit
def mergeSort2(lst):  # non-recursive version
    i = 1
    while i < len(lst):
        result = []
        for j in range(0, len(lst), 2 * i):
#            print lst[j:j+i]
            result += merge(lst[j:j+i], lst[j+i:j+2*i])
#            print result, i
        lst = result[:]
#        print lst
        i = i * 2
#        print i
    return lst
    
def partition(lst, low, high):
    i = low + 1
    j = high 
    while True:
        while lst[i] <= lst[low]:
            if i == high:
                break
            i += 1
        while lst[j] >= lst[low]:
            if j == low:
                break
            j -= 1
        
        if i >= j:
            break
        lst[i], lst[j] = lst[j], lst[i]
    lst[low], lst[j] = lst[j], lst[low]
#    print lst[:j], lst[j], lst[j+1:]
    return j

def qSort(lst, low, high):
    if high <= low:
        return lst
    mid = partition(lst, low, high)
    qSort(lst, low, mid-1)
    qSort(lst, mid+1,high)


def quickSort(lst):
    random.shuffle(lst)
#    print lst
    return qSort(lst, 0, len(lst)-1)

#mergeSort([91,84,39,71,88,73,93,63,45,95,59,22])
    

def sink(lst, k, length):
    while 2 * k <= length:
        j = 2 * k
        if j < length and lst[j-1] < lst[j] :  # 因为二叉堆的定义索引是从零开始的，所以看起来有点怪
            j += 1
        if lst[k-1] > lst[j-1]:
            break
        lst[k-1], lst[j-1] = lst[j-1], lst[k-1]
        k = j
@timeit
def heapSort(lst):
    length = len(lst)
    for i in xrange(length/2, 0, -1):
        sink(lst, i, length)
    while length > 1:
        lst[0], lst[length-1] = lst[length-1], lst[0]
        length -= 1
        sink(lst, 1, length)
    return lst

############################### A more intuitive solution ########
def swap(lst, i, j):
    lst[i-1], lst[j-1] = lst[j-1], lst[i-1]

def less(lst, i, j):
    return lst[i-1] < lst[j-1]

def sink2(lst, k, length):
    while 2 * k <= length:
        j = 2 * k
        if j < length and less(lst, j, j+1):
            j += 1
        if not less(lst, k, j):
            break
        swap(lst, j, k)
        k = j
@timeit
def heapSort2(lst):
    length = len(lst)
    for i in xrange(length/2, 0, -1):
        sink2(lst, i, length)
    while length > 1:
        swap(lst, 1, length)
        length -= 1
        sink2(lst, 1, length)
    return lst
###############################
#print heapSort([91,84,39,71,88,73,93,63,45,95,59,22])
#selectionSort(lst[:])
#insertionSort(lst[:])
#shellSort(lst[:])

#print mergeSort2([7,5,8,9,2,0])

#print quickSort([7,5,8,9,2,0])

def check_sorted(lst):
    for i in xrange(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True

if check_sorted(insertionSort(lst[:])):
    print 'insertionSort passed'
else:
    print 'not passed'
    
if check_sorted(selectionSort(lst[:])):
    print 'selectionSort passed'
else:
    print 'not passed'

if check_sorted(shellSort(lst[:])):
    print 'shellSort passed'
else:
    print 'not passed'
if check_sorted(mergeSort(lst[:])):
    print 'mergeSort passed'
else:
    print 'not passed'

t1 = time.time()
msorted = mergeSort(lst[:])
t2 = time.time()
if check_sorted(msorted):
    print 'time for mergeSort: %f' %(t2-t1)
else:
    print 'not passed'

if check_sorted(mergeSort2(lst[:])):
    print 'mergeSort2 passed'
else:
    print 'not passed'

#t1 = time.time()
qsorted = quickSort(lst[:])
t2 = time.time()
if check_sorted(qsorted):
    print 'time for quickSort: %f' %(t2-t1)
else:
    print 'not passed'

if check_sorted(heapSort(lst[:])):
    print 'heapSort passed'
else:
    print 'not passed'

if check_sorted(heapSort2(lst[:])):
    print 'heapSort2 passed'
else:
    print 'not passed'

