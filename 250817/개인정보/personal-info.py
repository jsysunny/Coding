n = 5

class Student:
    def __init__(self, name , height, weight ):
        self.name, self.height, self.weight= name, height, weight

student=[]
for _ in range(n):
    n, h, w = input().split()
    student.append(Student(n, int(h), float(w)))

student1=student.copy()
student.sort(key=lambda x: x.name)

print("name")
for stu in student:
    print(stu.name, stu.height, stu.weight)

print()

student1.sort(key=lambda x: -x.height)

print("height")
for stu in student1:
    print(stu.name, stu.height, stu.weight)