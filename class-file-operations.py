class MyfileOpen():
    """this is the class the lets
anyone play with a file"""
    def __init__(self,name):
        self.name=name
        self.contents=open(name).read()
    def getsize(self):
        """
The method will give the size of file in bytes."""
        print( len(self.contents))
    def getwordcount(self):
        print( len(self.contents.split()))
    def getlinecount(self):
        print( len(self.contents.split('\n')))
f=MyfileOpen('c:/users/tring/desktop/words.txt')
f.printfile()
f.getlinecount()
print(f.name)
print(dir(f))
help(f.getsize)
