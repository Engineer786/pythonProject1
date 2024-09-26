class Student:
    def setName(self, name):
        self.name = name

    def setMarks(self, marks):
        self.marks = marks

    def getName(self):
        return self.name

    def getMarks(self):
        return self.marks


n = int(input(f'Enter number of students: '))
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    s = Student()
    s.setName(name)
    s.setMarks(marks)
    res1 = s.getName()
    res2 = s.getMarks()
    print(f'Student Name: {res1}')
    print(f'Student Marks: {res2}')

