class Student:
    college_name ="ABC college"
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
stu1 = Student("Vaishu", 8.5)
stu2 = Student("Jay", 9.2)
print(stu1.name)
print(stu1.gpa)
print(Student.college_name)
print(stu2.name)
print(stu2.gpa)
print(Student.college_name)