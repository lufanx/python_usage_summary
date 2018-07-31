#!/usr/bin/env python

class FileHandle(object):
    def __init__(self, filePath, fileType):
        self.filePath = filePath
        self.fileType = fileType

    def openFile(self):
        try:
            self.f = open(self.filePath, self.fileType)
        except IOError,e:
            print (e)
            self.f.close()

    def writeFile(self):
        self.f.write("This is write\n")


def main():
    f1 = FileHandle('conf.ini', 'a+')
    f1.openFile()
    f1.writeFile()

if __name__ == "__main__":
    main()
