class Student:
    def __init__(self,name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):
        print(f'Student name: {self.name}')
        print(f'Student rollno: {self.rollno}')
        print(f'Student marks: {self.marks}')

    def grade(self):
        if self.marks >= 60:
            print(f'Student got first grade')
        elif self.marks >= 50:
            print(f'Student got second grade')
        elif self.marks >= 40:
            print(f'Student got third grade')
        else:
            print(f'Student are failed')


n = int(input('Enter a number of student: '))
for i in range(n):
    name = input('Enter student name: ')
    rollno = int(input('Enter student rollno: '))
    marks = int(input('Enter student marks: '))
    s = Student(name, rollno, marks)
    s.display()
    s.grade()
