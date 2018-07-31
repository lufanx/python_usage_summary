#!/usr/bin/env python

import threading
import time

def action(arg):
    time.sleep(1)
    print ("current thread name: %s\n" % threading.currentThread().getName())
    print ('the arg is %d\n' % arg)

def main():
    thread_list = []
    for i in xrange(4):
        t = threading.Thread(target=action, args = (i,))
        t.setDaemon(True)
        thread_list.append(t)
    for t in thread_list:
        t.start()
        
    for t in thread_list:
        t.join()

    print ('main thread end!')

if __name__ == "__main__":
    main()
