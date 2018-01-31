#!/usr/bin/env python

class A:
    def hello(self):
        print ("hello A")
class B(A):
    #pass
    def hello(self):
        print ("hello B")

a = A()
b = B()

print (a.hello())
print (b.hello())
