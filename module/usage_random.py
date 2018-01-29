#!/usr/bin/env python

import random

class Random:
    """these methods include random, randint, sample, shuffle, choice"""

    member = 0;
    def random(self):
        Random.member += 1
        ret = random.random()
        return ret

    def randint(self, a, b):
        #self.a = a
        #self.b = b
        Random.member += 1
        #ret = random.randint(self.a, self.b)
        ret = random.randint(a, b)
        return ret

    def choice(self, dts):
        Random.member += 1
        ret = random.choice(dts)
        return ret
    
    def sample(self, dts, val):
        Random.member += 1
        ret = random.sample(dts, val)
        return ret

    def shuffle(self, dts):
        Random.member += 1
        random.shuffle(dts)
        return dts

def main():
    test_random1 = Random()
    ret = test_random1.random()
    print (ret)
    print (test_random1.member)

    test_random2 = Random()
    ret = test_random2.randint(4, 10)
    print (ret)
    print (test_random2.member)

    test_random3 = Random()
    ret = test_random3.choice("hello world")
    print (ret)
    print (test_random3.member)

    test_random4 = Random()
    ret = test_random4.sample("hello world", 3)
    print (ret)
    print (test_random4.member)

    test_random5 = Random()
    ret = test_random5.shuffle([3, 5, 7, 9])
    print (ret)
    print (test_random5.member)

if __name__ == '__main__':
    main()
