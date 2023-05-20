from Student import Student
from Teacher import Teacher

s1 = Student(name='Trung Dung', major='CS', gpa=3.9)
s2 = Student(name='Diem Hang', major='FK', gpa=3.9)
s3 = Student(name='Trung Gau', major='AC', gpa=3.9)
t1 = Teacher(name='Jon', students=[s1, s2])
t2 = Teacher(name='Jil', students=[s1, s3])

s1.teachers = [t1, t2]
s2.teachers = [t1]
s3.teachers = [t2]

students = [s1, s2, s3]
teachers = [t1, t2]

for student in students:
    print(student)

for teacher in teachers:
    print(teacher)
