#!/usr/bin/env python

def main():
    name = 'zhangsan'
    age = 23 if name else 0
    print (age)
    
    test = [x * x for x in xrange(3)]
    print (test)

    test_list = [x * x for x in xrange(4) if x % 2 == 0]
    print (test_list)


if __name__ == "__main__":
    main()
