#!/usr/bin/env python

import time

class Time:
    """About time module include (time, localtime, gmtime, mktime, sleep, strftime)"""
    def time(self):
        ret = (int)(time.time())
        return ret
    
    def localtime(self, *args):
        if not args:
            ret = time.localtime()
            return ret
        for i in args:
            ret = time.localtime(i)
            return ret

    def gmtime(self, *args):
        if not args:
            ret = time.gmtime()
            return ret
        for i in args:
            ret = time.gmtime(i)
            return ret

    def mktime(self):
        ret = time.mktime(time.localtime())
        return ret

    def sleep(self, second):
        self.second = second
        time.sleep(self.second)
        print ('pringing...')

    def strftime(self):
        #ret = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        ret = time.strftime("%Y-%m-%d %H:%M:%S")
        return ret

def main():
    test_time1 = Time()
    ret = test_time1.time()
    print (ret)

    test_time2 = Time()
    ret = test_time2.localtime()
    print (ret)

    test_time3 = Time()
    ret = test_time3.localtime(167469823)
    print (ret)

    test_time4 = Time()
    ret = test_time4.gmtime(187469823)
    print (ret)

    test_time5 = Time()
    ret = test_time5.gmtime()
    print (ret)

    test_time6 = Time()
    ret = test_time6.mktime()
    print (ret)

    test_time7 = Time()
    test_time7.sleep(5)

    test_time8 = Time()
    ret = test_time8.strftime()
    print (ret)
    

if __name__ == '__main__':
    main()
