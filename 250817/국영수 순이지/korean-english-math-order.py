n = int(input())
name = []
korean = []
english = []
math = []

class Score:
    def __init__ (self, name, korean, english, math):
        self.name, self.korean, self.english, self.math= name, korean, english, math

score=[]
for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))
    score.append(Score(student_info[0], int(student_info[1]),int(student_info[2]), int(student_info[3])))

score.sort(key=lambda x: (-x.korean, -x.english, -x.math))

for i in range(n):
    print(score[i].name, score[i].korean, score[i].english, score[i].math)

# Please write your code here.