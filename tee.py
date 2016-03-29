#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

import sys

def tee(filename):
    with open(filename, 'w') as f:
        for line in sys.stdin.readlines():
            sys.stdout.write(line)
            f.write(line)

if __name__ == '__main__':
    filename = sys.argv[1]
    tee(filename)

