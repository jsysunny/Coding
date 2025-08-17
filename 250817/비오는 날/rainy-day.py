n = int(input())
date = []
day = []
weather = []

class Rain:
    def __init__(self, dates, week, weathers):
        self.dates= dates
        self. week= week
        self. weathers= weathers

all=[]
for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)
    all.append(Rain(d, dy,w))

for i in range(n):
    if all[i].weathers=='Rain':
        print(all[i].dates, all[i].week, all[i].weathers)
        break
# Please write your code here.



