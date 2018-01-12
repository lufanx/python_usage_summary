#!/usr/bin/env python

def main():
    test_list = [1, 4, 6, 'zhangsan', 9, 'lisi']
    list_operate(test_list)
    list_operate_more(test_list)
    list_function_operate(test_list)
    list_order_operate(test_list)

def list_operate(test_list):
    print test_list[0]
    print test_list[:]
    print test_list[:3]
    print test_list[3:]

def list_operate_more(test_list):
    print test_list + [10, 11]
    print test_list * 2

def list_function_operate(test_list):
    i = None
    
    print "i = {}".format(len(test_list))
    print "i = %d" % len(test_list)

    for n in test_list:
        print n

    if 'zhangsan' in test_list:
        print True

    max_val = max(test_list)
    min_val = min(test_list)
    print "max_val = {0} min_val = {1}".format(max_val, min_val)

    cmp_list = [1, 4, 6, 'lisi']
    cmp_re = cmp(test_list, cmp_list)
    print "cmp_re = {}".format(cmp_re)

def list_order_operate(test_list):
    test_list.append(13)
    print test_list

    print test_list.count(6)

    test_list.extend([19, 20])
    print test_list
    print test_list.index(4)

    test_list.insert(0, 0)
    print test_list

    test_list.pop()
    print test_list

    test_list.remove(1)
    print test_list

    test_list.reverse()
    print test_list

    test_list.sort()
    print test_list

if __name__ == "__main__":
    main()
