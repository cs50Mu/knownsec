#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

import string

def camelTrans(s):
    result = ''
    for i in s:
        if i in string.uppercase:
            result += '_' + i.lower()
        else:
            result += i
    return result


print camelTrans('getShopId')
