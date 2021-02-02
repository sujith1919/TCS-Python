import os
import time
class FileInfo:
    def __init__(self,name):
        self.filename = name
        self.f=open(self.filename,'r')
        self.lines = self.f.readlines()
        
    def getfilesize(self):
        print(os.path.getsize(self.filename))
    def getlinecount(self):
        print(len(self.lines))
    def getcreationtime(self):
        print(time.ctime(os.path.getctime(self.filename)))
    def firstline(self):
        self.nthline(1)
    def lastline(self):
        self.nthline(0)
    def nthline(self,lineno):
        print(self.lines[lineno - 1])
    def close(self):
        self.f.close()
    def getage(self):
        age = time.time() - (os.path.getctime(self.filename))
        print("File age is {} days".format(round(age/60/60/24,2)))
    def search(self,searchstring):
        for lineno,line in enumerate(self.lines):
            if searchstring in line:
                print(lineno +1, line, end="")
