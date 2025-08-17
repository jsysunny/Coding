
n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]
#print(students)
# Please write your code here.
class Student:
    def __init__(self, height, weight, number):
        self.height, self.weight, self.number = height, weight,number

students=[Student(h,w,n) for h,w,n in students]

students.sort(key=lambda x: (x.height, -x.weight))

for student in students:
    print(student.height, student.weight, student.number)


# Please write your code here.