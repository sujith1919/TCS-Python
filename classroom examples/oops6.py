class Employee:
    _count=0  #private class variable
    def __init__(self,eid,name,mobile):
        self.eid=eid
        self.name=name
        self.mobile=mobile
        Employee._count+=1
    def get_mobile(self):
        print(self.mobile)
    def set_mobile(self,mobile):
        self.mobile=mobile
    @classmethod
    def get_count(cls):
        print(cls._count)

Employee.get_count()
ramesh = Employee(223,'Ramesh','9885970033')
suresh = Employee(256,'Suresh','9665970033')
ramesh.get_count()
Employee.get_count()

