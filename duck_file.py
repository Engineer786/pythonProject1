from abc import *
class Employee:
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal
    def __mul__(self, other):
        return self.sal*other.days

class TimeSheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days

    def __mul__(self, other):
        return self.days*other.sal



e = Employee('saheb', 1000)
#e1 = Employee('Sohrab', 1000)
t = TimeSheet('saheb', 20)
print(f'Total this month salary for saheb: {e*t}')

class P:
    def m1(self):
        print('parent class method')

class C(P):
    def m1(self):
        print('child class method')


c1 = C()
c1.m1()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display(self):
        print(f'Employee Name: {self.name}')
        print(f'Employee Age: {self.age}')
        print(f'Employee Salary: {self.salary}')


e = Employee('saheb', 31, 40000)
e = Employee('sohrab', 6, 10000)
e.display()
print()
e.display()
print()
print('Abstract class here')
class Vehicle(ABC):
    @abstractmethod
    def getNoOfWheels(self):
        pass

class Car(Vehicle):
    def getNoOfWheels(self):
        return 4

class Bus(Vehicle):
    def getNoOfWheels(self):
        return 6


c = Car()
print('Car has',c.getNoOfWheels(),'wheels')
b = Bus()
print('Bus has',b.getNoOfWheels(),'wheels')
print()
class CollegeAutomation(ABC):
    @abstractmethod
    def updateMarks(self):
        pass
    @abstractmethod
    def getFeeDetails(self):
        pass
    @abstractmethod
    def admissionDetails(self):
        pass

class StudentMarks(CollegeAutomation):
    def updateMarks(self):
        print('marks is upfated')
    def getFeeDetails(self):
        print('Student fee is submitted')

class ConcreteCls(StudentMarks):
    def admissionDetails(self):
        super().updateMarks()
        super().getFeeDetails()
        print('admission is over')


s = ConcreteCls()
s.admissionDetails()
print()
class Test:
    def __init__(self):
        self.__x = 10


t1 = Test()
print(t1._Test__x)
print()
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def __str__(self):
        return f'Student name : {self.name} and rollno : {self.rollno}'

s1 = Student('saheb', 2)
s2 = Student('sohrab', 3)
print(s1)
print(s2)