MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

class Name:
    def __init__(self, codename, score):
        self. codename= codename
        self.score=score

name=[]
# Please write your code here.
for i in range(len(codenames)):
    name.append(Name(codenames[i], scores[i]))

mina=100

for i in range(len(name)):
    if name[i].score < mina:
        mina = name[i].score

for i in range(len(name)):
    if name[i].score==mina:
        print(name[i].codename, name[i].score)

    