class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f'Employee name: {self.name}')
        print(f'Employee salary: {self.salary}')

    # def setEmpId(self, empId):
    #     self.empId = empId
    #
    # def getEmpId(self):
    #     self.dispaly()
    #     return self.empId
class Employee(Person):
    def __init__(self, name, salary, empid):
        super().__init__(name, salary)
        self.empid = empid

    def dispaly1(self):
        self.display()
        print(f'Employee Empid: {self.empid}')


e1 = Employee('saheb', 5000, 100)
e1.dispaly1()
#e1.setEmpId(100)
#print(f'Employee Id: {e1.getEmpId()}')