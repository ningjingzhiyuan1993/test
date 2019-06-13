#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Sauron'

import sys
import numpy

def test():
    argv = sys.argv
    if len(argv) == 1:
        print('hello, world')
    elif len(argv) == 2:
        print('hello, %s' % argv[1])
    else:
        print('too much arguments')

if __name__ == '__main__':
    test()
