#!/usr/bin/env python


import threading
import time

def action(arg):
    time.sleep(1)
    print ("the arg is: %d\n" % arg)

def main():
    for i in xrange(4):
        t = threading.Thread(target=action, args=(i,))
        t.start()

    time.sleep(3)
    print "main thread end!"

if __name__ == "__main__":
    main()
