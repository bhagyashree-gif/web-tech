'''class Student:
    name = "ram"
    age = 20

s1 = Student()
s2 = Student()

s1.name = "Ramu"
s2.name = "Raju"

print(s1.name)
print(s2.name)
print(Student.name)'''


'''class College:
    name = "Gopalan college"
    loc = "Hoodi"

s1 = College()

s1.name = "Raju"
s1.age = 20
s1.dept = "ISE"

print(s1.name, s1.age, s1.dept)'''


''''class College:
    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

    def display(self):
        print(self.name, self.age, self.dept)


s1 = College("Raju", 20, "CSE")
s2 = College("Ramu", 22, "ISE")

s1.display()
s2.display()'''


'''
class Student:
    name = "Gopalan college"
    loc = "Hoodi"

    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

    def display(self):
        print(self.name, self.age, self.dept)

    def change_name(self, new):
        self.name = new


s1 = Student("Raju", 20, "CSE")
s2 = Student("Ram", 22, "ISE")

print("Before")
s2.display()

s2.change_name("Ramu")

print("After")
s2.display()'''


class college:
    name='Gopalan college'
    loc='Hoodi'

    @classmethod
    def disp(cls):
        print(cls.name,cls.loc)
    @classmethod
    def change_loc(cls,new):
        cls.loc=new

    def __init__(self,name,age,dept):
        self.name=name
        self.age=age
        self.dept=dept
    def display(self):
        print(self.name,self.age,self.dept)
    def change_name(self,new):
        self.name=new
s1=college("raju",20,"ise")
s2=college("ramu",20,"ise")
print("Before")
s2.display()
s2.change_name("ramu")
print("After")
s2.display()
print('------------')
college.change_name(s1,"raj")
college.display(s1)
print(s1.name)
print('--------')
college.change_name(s1,"Raj")
college.display(s1)
print(s1.name)
print('--------')
s1.disp()
s2.disp()
college.change_loc("E.city")
college.disp()
print(s1.loc)