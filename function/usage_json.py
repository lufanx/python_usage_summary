#!/usr/bin/env python

# -*- coding: utf-8 _*_

import json

dict_info = {
                'A': {
                        'name': 'zhangsan',
                        'age': 25,
                        'six': 'f'
                    },
                'B': {
                        'name': 'lisi',
                        'age': 24,
                        'six': 'f'
                    }
    
            }


class Json:
    
    def dump(self):
        with (open('dict.log', 'a+')) as f:
            f.seek(0)
            json.dump(dict_info, f)
            f.close()

    def load(self):
        with (open('dict.log', 'r')) as f:
            print (json.load(f))
            f.close()

    def write(self):
        with (open('dict.log', 'a+')) as f:
            f.write(str(dict_info))
            f.close()

def main():

    """write ways, as str write file"""
    test_json3 = Json()
    test_json3.write()

    """dump way, as json format write file"""
    test_json1 = Json()
    test_json1.dump()

    test_json2 = Json()
    test_json2.load()


if __name__ == '__main__':
    main()

