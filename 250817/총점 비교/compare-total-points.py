n = int(input())

name = []
score1 = []
score2 = []
score3 = []

class Score:
    def __init__ (self, name, korean, english, math):
        self.name, self.korean, self.english, self.math= name, korean, english, math

score=[]
for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))
    score.append(Score(student_input[0], int(student_input[1]),int(student_input[2]), int(student_input[3])))

score.sort(key=lambda x:x.korean+x.english+x.math)
for i in range(n):
    print(score[i].name, score[i].korean, score[i].english, score[i].math)


# Please write your code here.
