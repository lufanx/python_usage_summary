#!/usr/bin/env python

from tabulate import tabulate

def main():
	print ("table format".center(50, '*'))
	table = [['zhangsan', '30'], ['lisi', '21'], ['wangwu', '40']]
	print (tabulate(table, headers=['Name', 'Age']))
	print ("table format".center(50, '*'))

if __name__ == "__main__":
	main()
