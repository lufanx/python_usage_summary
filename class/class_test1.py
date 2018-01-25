#!/usr/bin/env python

class Person:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print ("hello world!, I'm %s." % self.name)

foo = Person()
bar = Person()
foo.setName('Luke SKywalker')
bar.setName('Anakin SKwalker')
foo.greet()
bar.greet()

print (foo.name)
bar.name = 'Yoda'
bar.greet()
