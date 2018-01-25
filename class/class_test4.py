#!/usr/bin/env python

class Secretive:
    def __inaccessible(self):
        print ('Bet you can\'t see me...')

    def accessible(self):
        print ('The secret message is')
        self.__inaccessible()

s = Secretive()

# This usage is error, it is inaccessible, not is accessible
#s.__inaccessible()

# The usage is true.
s._Secretive__inaccessible()

s.accessible()
