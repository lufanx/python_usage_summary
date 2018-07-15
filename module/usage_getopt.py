#!/usr/bin/env python

import getopt
import sys

def usage():
    print ("==========")
    print ("Args:")
    print ("    -i 127.0.0.1 -p 8009")
    print ("    --ip=127.0.0.1 --port=8009")
    print ("==========")

def main():

    # python usage_getopt.py -h
    # python usage_getopt.py --help
    # python usage_getopt.py -i 127.0.0.1 -p 8009 77 99
    # python usage_getopt.py --ip=127.0.0.1 -port=8009
    # python usage_getopt.py --ip=127.0.0.1 -port=8009 66 88
    options, args = getopt.getopt(sys.argv[1:], "hp:i:", ["help", "ip=", "port="])

    for name, values in options:
        if name in ("-h", "--help"):
            usage()
        if name in ("-i", "--ip"):
            print ("value: {0}".format(values))
        if name in ("-p", "--port"):
            print ("value: {0}".format(values))
    for name in args:
        print ("name: {0}".format(name))

if __name__ == "__main__":
    main()
