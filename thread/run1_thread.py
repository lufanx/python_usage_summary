#!/usr/bin/env python

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg
    def run(self):
        self.action()

    def action(self):
        time.sleep(1)
        print ('current thred name: %s\n' % threading.currentThread().getName())
        print ('the arg is: %d\n' % self.arg)

def main():
    for i in xrange(4):
        t = MyThread(i)
        t.start()

    time.sleep(3)
    print ('main thread end!')

if __name__ == "__main__":
    main()
