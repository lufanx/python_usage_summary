#!/usr/bin/env python

# -*- coding: utf-8 -*-

def main():

    """print []"""
    print (eval('[]')) 

    """print 3"""
    print (eval('1 + 2'))

    """False"""
    ret = all([0, 1, 2, 3, 4])
    print (ret)

    """True"""
    ret = any([0, 1, 2, 3, 4])
    print (ret)

    """X, print chr"""
    ret = chr(88)
    print (ret)

    """35, print ASCII"""
    ret = ord('#')
    print (ret)

if __name__ == '__main__':
    main()
