#!/usr/bin/env python

class SelfNumError(Exception):
    def __init__(self, errorInfo):
        super(SelfNumError, self).__init__()
        self.errorInfo = errorInfo

def main():
    try:
        x = 5/5
        if x == 1:
            raise SelfNumError("x not i")
    except SelfNumError,e:
        print (e.errorInfo)

if __name__ == "__main__":
    main()
