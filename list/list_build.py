#!/usr/bin/env python


def main():
	list = [1, 2, "zhangsan", 4, 6]
	list_operate(list)

	list_function(list)
	list_method(list)

def list_operate(list):
	list += [7, 8]
	print list

	if 1 in list:
		print "1 in list"
	
	for i in list:
		print i

	list_1 = ["hi"]
	list_1 *= 3
	print list_1

def list_function(list):
	"""
		this function include:
				max :return max value 
				min :return min value
				len :count len
				cmp : cmp 2 list
				list :will yuanzu change list
	"""
	max_num = max(list)
	print max_num
	min_num = min(list)
	print min_num
	count = len(list)
	print count
	list_2 = [1, 2]
	cmp_ll = cmp(list, list_2)
	print cmp_ll


def list_method(list):
	"""
		append, count, extend, index, insert, pop, remove, reverse, sort.
	"""
	list.append(9)
	print list
	cycles = list.count(1)
	print cycles
	list_4 = [13,14]
	list.extend(list_4)
	print list
	index = list.index(9)
	print index
	list.insert(2, 2)
	print list
	list.pop()
	print list
	list.remove(2)
	print list
	list.reverse()
	print list
	list.sort()
	print list


if __name__ == "__main__":
	main()
