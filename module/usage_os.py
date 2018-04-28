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

    def path_isdir(self):
        if os.path.isdir('/tmp'):
            print ('/tmp is dir')
        else:
            print ('/tmp not is dir')

    def path_isfile(self):
        if os.path.isfile('/tmp'):
            print ('/tmp is file')
        else:
            print ('/tmp not is file')

    def path_exists(self):
        if os.path.exists('/tmp'):
            print ('exist tmp dir or file')
        else:
            print ('not exist tmp dir or file')

    def path_basename(self):
        """return 'file'"""
        return os.path.absname('/tmp/file')

    def path_dirname(self):
        """retunr 'tmp'"""
        return os.path.dirname('/tmp/file')


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
test1.path_isdir()
test1.path_isfile()
test1.path_exists()
test1.path_absname()
test1.path_dirname()
