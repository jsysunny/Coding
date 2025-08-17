n = int(input())
name = []
height = []
weight = []

class Student:
    def __init__(self, name, height, weight):
        self.name=name
        self.height=height
        self.weight=weight

student=[]
for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))
    student.append(Student(n_i,h_i,w_i))

student.sort(key=lambda x : x.height)

for i in range(n):
    print(student[i].name, student[i].height, student[i].weight)
# Please write your code here.
