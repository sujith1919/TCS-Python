import os
class FileInfo:
    def __init__(self,fname):
        self.fname=fname
        self.f=open(self.fname,'r')
        self.lines=self.f.readlines()
    def firstline(self):
        self.nthline(1)
    def lastline(self):
        self.nthline(0)
    def nthline(self,lno):
        print(self.lines[lno-1].rstrip())
    def getsize(self):
        print(os.stat(self.fname).st_size)
    def close(self):
        self.f.close()
