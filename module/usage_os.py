#!/usr/bin/env python

import os

class System:
    def getcwd(self):
        print (os.getcwd())
    
    def chdir(self):
        os.chdir('/home')
        print (os.getcwd())

    def listdir(self):
        """
            return 'python_usage_summary' dir below dir list
        """
        print (os.listdir('/home/fl/python_usage_summary'))
    
    def mkdir(self):
        os.mkdir('/tmp/test2')

    def rmdir(self):
        os.rmdir('/tmp/test2')

    def makedirs(self):
        os.makedirs('/tmp/a/b/c')

    def removedirs(self):
        os.removedirs('/tmp/a/b/c')

    def rename(self):
        os.rename('/tmp/test.txt', '/tmp/test2.log')

    def stat(self):
        print (os.stat('/tmp/test2.log'))

    def system(self):
        print (os.system('ls -al'))

    def getenv(self):
        print (os.getenv('PATH'))

    def curdir(self):
        """print . char"""
        print (os.curdir)
    
    def pardir(self):
        """print .. char"""
        print (os.pardir)

    def name(self):
        print (os.name)


test1 = System()
test1.getcwd()
test1.chdir()
test1.listdir()
#test1.mkdir()
#test1.makedirs()
#test1.rmdir()
#test1.removedirs()
#test1.rename()
test1.stat()
test1.system()
test1.getenv()
test1.curdir()
test1.pardir()
test1.name()
