class Employee:
    count=0  #class variable
    def __init__(self,eid,name,mobile):
        self.eid=eid
        self.name=name
        self.mobile=mobile
        Employee.count+=1
    def get_mobile(self):
        print(self.mobile)
    def set_mobile(self,mobile):
        self.mobile=mobile

ramesh = Employee(223,'Ramesh','9885970033')
ramesh.get_mobile()
ramesh.set_mobile("1233456677")
ramesh.get_mobile()
print(ramesh.count)
suresh = Employee(256,'Suresh','9665970033')
print(Employee.count)
