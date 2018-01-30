#!/usr/bin/env python

import hashlib

class Hashlib:
    """about hashlib.md5 module method test"""
    def md5(self, md5_str):
        re = md5_str.encode()
        ret = hashlib.md5(re)
        return ret.hexdigest()

def main():
    test_md5 = Hashlib()
    ret = test_md5.md5("12345")
    print (ret)


if __name__ == '__main__':
    main()
