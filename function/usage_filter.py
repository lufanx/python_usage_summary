#!/usr/bin/env python

# -*- coding: utf-8 -*-

def func(num):
    if num % 2 == 0:
        return True
    else:
        return False

def main():
    nums = [x for x in range(1, 11)]
    ret = filter(func, nums)
    print (list(ret))


if __name__ == '__main__':
    main()
