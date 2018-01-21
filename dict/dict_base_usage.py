#!/usr/bin/env python
from copy import deepcopy

def format_print():
    tem = '''
    name = %(name)s
    age = %(age)d
    '''
    tem_info = {}
    tem_info['name'] = 'lisi'
    tem_info['age'] = 24
    tem = tem % tem_info
    print tem

def clear_function(d):
    d.clear()
    # d is {}
    print d

def copy_function():
    copy_before = {}
    copy_before['name'] = 'lisi'
    copy_before['age'] = 24
    copy_before['skill'] = ['write', 'read']
    dts = copy_before.copy()
    st = deepcopy(copy_before)
    print dts
    dts['name'] = 'zhangsan'
    dts['skill'].remove('read')
    st['skill'].remove('read')
    print dts
    print copy_before
    print st

def get_function():
    d = {}
    d['name'] = 'zhangsan'
    d['age'] = 24

    if d.get('name'):
        print 'have this key'
    else:
        print 'not this key'
    if 'name' in d:
        print 'name in d'
    else:
        print 'name not in d'

def items_iteritems_function():
    d = {}
    d['name'] = 'lisi'
    d['age'] = 24
    
    print d.items()
    for k, v in d.items():
        print 'd[{0}] = {1}'.format(k, v)
    
    for k, v in d.iteritems():
        print 'd[{0}] = {1}'.format(k, v)

def keys_function():
    d = {}
    d['name'] = 'lisi'
    d['age'] = 25

    print d.keys()
    for k in d.iterkeys():
        print k

def pop_function():
    d = {}
    d['name'] = 'lisi'
    d['age'] = 24
    d.pop('name')
    print d

def setdefault_function():
    d = {}
    d.setdefault('name', 'lisi')
    print d

def update_function():
    d = {
        'title' : 'python web site',
        'url' : 'www.python.ory'
    }
    x = {'title' : 'hello python'}
    d.update(x)
    print d

def values_itervalues_function():
    d = {}
    d['name'] = 'lisi'
    d['age'] = 12

    print d.values()
    for value in d.itervalues():
        print value

def main():
    d = {}
    d['name'] = 'lisi'
    d['age'] = 24
    format_print()
    clear_function(d)
    # d is {}
    print d
    copy_function()
    get_function()
    items_iteritems_function()
    keys_function()
    pop_function()
    setdefault_function()
    update_function()
    values_itervalues_function()



if __name__ == '__main__':
    main()
