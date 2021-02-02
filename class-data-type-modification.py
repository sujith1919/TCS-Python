class MyList(list):
    def __add__(self,other):
		tmplist=[]
		for x in range(len(self)):
			tmplist.append(self[x]+other[x])
		return tmplist
		
a=MyList()
a.append(1)
a.append(3)
a.append(4)

b=MyList([7,8,9])

print a+b