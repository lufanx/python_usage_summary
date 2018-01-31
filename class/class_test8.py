#!/usr/bin/env python

__metaclass__ = type

class Bind:
    def __init__(self):
        self.song = "hung"
    def est(self):
        if self.song == "hung":
            print ("this hung")


class Song(Bind):
    def __init__(self):
        #Bind.__init__(self)
        super(Song, self).__init__()
        self.c = "hu"
    def sing(self):
        if self.c == "hu":
            print ("this is sing")

a = Bind()
print (a.est())

b = Song()
print (b.sing())
print (b.est())
