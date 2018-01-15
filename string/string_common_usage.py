#!/usr/bin/env python

def start_main():
    str = "Hello python"

    lower_str = str.lower()

    print lower_str

    str_list = ['1', '2', '3', '4']
    sep = '+'

    print sep.join(str_list)

    str_list_split = "1+2+3+4"
    print str_list_split.split('+')

    str_check = '4'

    if str_check.isdigit():
        print "str_check is digit"

    str_str = 'hello world'

    i = str_str.find('world')
    print i

if __name__ == "__main__":
    start_main()
