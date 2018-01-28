#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')

if config.has_section('Info'):
    print ('already exist this section')
else:
    print ('not exist thie section')
    print ('will create this section:')
    config.add_section('Info')
    config.write(open('config.ini', 'w'))
    config.set('Info', 'name', 'zhangsan')
    config.write(open('config.ini', 'w'))

ret_sections = config.sections()
print (ret_sections)

ret_items = config.items('Info')
print (ret_items)

ret_options = config.options('Info')
print (ret_options)

ret_value = config.get('Info', 'name')
print (ret_value)
