class Project(object):
    store={}
    def __init__(self,name):
        self.name=name
        Project.store[self.name]=[] #create a list for every project
    def add(self,emp):
        if isinstance(emp,Employee):
            Project.store[self.name].append(emp)
            emp.project=self.name
            
        else: print "Only employees can be added"
    def __len__(self):return len(Project.store[self.name])
    def __iter__(self):
        self.last=0
        return self
    def next(self):
        if self.last<len(Project.store[self.name]):
            empname=Project.store[self.name][self.last].name
            self.last+=1
            return empname
        else:
            raise StopIteration

class Employee(object):
    def __init__(self,eid,name):
        self.eid=eid
        self.name=name
        self.project=''


satya=Employee(245,'Satya Nadella')
steve=Employee(175,'Steve Balmer')
gates=Employee(2,'Bill Gates')
ramesh="Employee(223,'Ramesh Sannareddy')"

ms=Project('Microsoft')
ms.add(satya)
ms.add(gates)
ms.add(steve)
ms.add(ramesh)

for emp in ms:print emp
        
print len(ms)


print satya.project
