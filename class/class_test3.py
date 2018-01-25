#!/usr/bin/env python

class Bird:
    song = 'Squaawk!'
    def sing(self):
        print (self.song)

bird = Bird()
bird.sing()
birdsong = bird.sing
birdsong()
