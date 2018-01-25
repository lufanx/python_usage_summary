#!/usr/bin/env python

class MemberCounter:
    member = 0
    
    def init(self):
        MemberCounter.member += 1

m1 = MemberCounter()
m1.init()

print (MemberCounter.member)

m2 = MemberCounter()
m2.init()

print (MemberCounter.member)

m1.member = 'Two'
print (m1.member)

print (m2.member)
