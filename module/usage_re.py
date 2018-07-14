#!/usr/bin/env python

import re

class Req(object):
    def __init__(self):
        pass

    def reCompile(self, *args):
        #rr = re.compile('[a-zA-Z]oo[a-zA-z]')
        if not args:
            exit()
        else:
            for i in args:
                rr = re.compile(i, re.I)
                return rr

def main():

    # re.findall all
    testStr1 = "Tina is a good girl, she is cool, clevel, and so on..."
    re1 = Req()
    rr = re1.reCompile('[a-zA-z]oo[a-zA-Z]')
    print (rr.findall(testStr1))


    # re.match head
    testStr2 = "comwww.runcomoob"
    re2 = Req()
    rr = re2.reCompile('com')
    print (rr.match(testStr2).group())


    # re.search first
    testStr3 = "www.4comrunoob.5com"
    re3 = Req()
    rr = re3.reCompile('com')
    print (rr.search(testStr3).group())

    # re.split as num split
    print (re.split('[0-9]', 'one1two2three3fore4file'))

    # re.sub, will ' ' ues '-' replace
    print (re.sub(' ', '-', testStr1))

    testStr4 = "juiehwuifi13513980873"
    print (re.findall('[0-9]{11}', testStr4))

    testStr5 = "kfkskkfk13509875656@163.com"
    print (re.findall(r'[0-9a-zA-Z_]{11}@[0-9a-zA-Z]{1,11}.[com,cn,net]{1,3}', testStr5))


if __name__ == "__main__":
    main()
