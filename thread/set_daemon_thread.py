#!/usr/bin/env python

import threading
import time

def action(arg):
    time.sleep(1)
    print ('current thread name: %s\n' % threading.currentThread().getName())
    print ('the arg is: %d\n' % arg)

def main():
    for i in xrange(4):
        t = threading.Thread(target = action, args = (i,))
        t.setDaemon(True)
        t.start()

    #time.sleep(1)
    print "main thread end!"

if __name__ == "__main__":
    main()
