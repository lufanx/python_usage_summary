#!/usr/bin/env python

def main():
    f = open('conf.ini', 'r')
    f1 = open('copy_conf.ini', 'w')

    while True:
        line = f.readline()
        if not line:break
        f1.write(line)

    f.close()
    f1.close()

if __name__ == "__main__":
    main()
