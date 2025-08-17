n = int(input())

class Student:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight=name, height, weight

student=[]
for _ in range(n):
    n_i, h_i, w_i = input().split()
    student.append(Student(n_i,int(h_i),int(w_i)))

student.sort(key=lambda x:(x.height, -x.weight))
for s in student:
    print(s.name, s.height, s.weight) 
# Please write your code here.