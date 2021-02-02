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
    def get_salary(self,days):
        print(days * 1000)
    @classmethod
    def get_count(cls):
        print(cls._count)

ramesh=Employee(223,"Ramesh S","9885970033")
ramesh.get_salary(21)

class Trainee(Employee):
    def __init__(self,eid,name,mobile,college):
        self.college=college
        super().__init__(eid,name,mobile)
    def get_salary(self,days):
        print(days * 100)

    def get_emp_salary(self,days):
        super().get_salary(days)

suresh=Trainee(678,"Suresh","9876534234","BITS")
suresh.get_salary(21)
suresh.get_emp_salary(21)
print(suresh.college)
print(suresh.eid)
Employee.get_count()
Trainee.get_count()


