class Employee:
    def __init__(self, name, age, sal):
        self.name = name
        self.age = age
        self.sal = sal

    def dispaly(self):
        print(f'Employee name: {self.name}')
        print(f'Employee age: {self.age}')
        print(f'Employee salary: {self.sal}')
    @classmethod
    def print(cls, emp_id):
        cls.emp_id = emp_id
    @staticmethod
    def show(comp):
        return comp


emp = Employee('saheb', 30, 40000)
emp.dispaly()
Employee.print('101')
print(f'Employee id: {Employee.emp_id}')
cmp = Employee.show('Microden')
print(f'Company name: {cmp}')
print()
# single level inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, sal, emp_id):
        super().__init__(name, age)
        self.sal = sal
        self.emp_id = emp_id

    def display(self):
        print(f'Employee name: {self.name}')
        print(f'Employee age: {self.age}')
        print(f'Employee sal: {self.sal}')
        print(f'Employee id: {self.emp_id}')



emp1 = Employee('sohrab khan', 4, 1000, 200)
emp1.display()
print()
# Multilevel inheritance
class Person(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Customer(Person):
    def __init__(self, name, age, product):
        super().__init__(name, age)
        self.product = product

class CustomerId(Customer):
    def __init__(self,name, age, product, cid):
        super().__init__(name, age, product)
        self.cid = cid


cd = CustomerId('faiz alam', 32, 'laptop', 'fz120')
print(f'Customer name: {cd.name}')
print(f'Customer age: {cd.age}')
print(f'Customer product: {cd.product}')
print(f'Customer cid: {cd.cid}')
print()
# Multiple inheritance
class A:
    def __init__(self):
        self.x = 10
class B:
    def __init__(self):
        self.y = 20

class C(A, B):
    def __init__(self):
        super().__init__()
        B.__init__(self)
        self.z = 30

    def display(self):
        print(f'x value: {self.x}')
        print(f'y value: {self.y}')
        print(f'z value: {self.z}')


c1 = C()
c1.display()
print()
# Hirarchical inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, rno, fees):
        super().__init__(name, age)
        self.rno = rno
        self.fees = fees

    def display(self):
        print(f'Student Name: {self.name}')
        print(f'Student age: {self.age}')
        print(f'Student roll no: {self.rno}')
        print(f'Student fees: {self.fees}')

class Teacher(Person):
    def __init__(self, name, age, sal, subject):
        super().__init__(name, age)
        self.sal = sal
        self.subject = subject

    def print(self):
        print(f'Teacher name: {self.name}')
        print(f'Teacher age: {self.age}')
        print(f'Teacher sal: {self.sal}')
        print(f'Teacher subject: {self.subject}')



s1 = Student('alam', 20, 101, 4000)
s1.display()
print()
t1 = Teacher('Danish', 27, 45000, 'English')
t1.print()

