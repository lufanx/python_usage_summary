#!/usr/bin/env python

# -*- coding; utf-8 -*-

def main():
    num1 = [x for x in range(1, 11)]
    num2 = ['zhangsan', 'lisi', 'wangwu', 'linch']

    print (list(zip(num1, num2)))

    for id_num, num in zip(num1, num2):
        print ('%d : %s' % (id_num, num))

if __name__ == '__main__':
    main()
