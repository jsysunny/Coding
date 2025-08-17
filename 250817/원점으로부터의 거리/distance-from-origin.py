n = int(input())

class Points:
    def __init__(self, x,y,num):
        self.x, self.y,self.num= x,y,num
# Please write your code here.
points=[]
for i in range(n):
    x,y= tuple(map(int, input().split())) 
    points.append(Points(x,y,i+1))

points.sort(key=lambda a: abs(a.x)+abs(a.y))

for p in points:
    print(p.num)

