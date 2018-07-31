#!/usr/bin/env python

class FileHandle(object):
    def __init__(self, filePath, fileType, fileFlush):
        self.filePath = filePath
        self.fileType = fileType
        self.fileFlush = fileFlush
    
    def openFile(self):
        try:
            self.f = open(self.filePath, self.fileType, self.fileFlush)
        except IOError,e:
            print (e)
            self.f.close()
    
    def readFile(self):
        return self.f.read()

    def closeFile(self):
        self.f.close()

def main():
    f1 = FileHandle('conf.ini', 'r', 1)
    f1.openFile()
    readValues = f1.readFile()
    print (readValues)

if __name__ == "__main__":
    main()
