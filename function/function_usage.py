#!/usr/bin/env python

def my_power(mun, n = 2):
    i = 1
    val = 1
    while (i <= n):
        val = val * mun
        i += 1
    return val


def first_usage():
    '''about power valuse'''
    
    val = my_power(5)
    print (val)
    
def my_two(*args):
    for i in args:
        print (i),
    print

def two_usage():
    my_two(1, 2, 3)
    test_list = [4, 5, 6]
    my_two(*test_list)

def print_info(name, age, city = 'shanghai'):
    print ('name : %s age : %d city: %s' % (name, age, city))

def three_usage():
    print_info('zhang san', 34, 'beijing')

def my_fore(**kw):
    print (kw)

def fore_usage():
    test_dict = {'name':'lisi', 'age':34, 'city':'shengzhen'}
    my_fore(**test_dict)

def main():
    first_usage()
    two_usage()
    three_usage()
    fore_usage()


if __name__ == '__main__':
    main()
