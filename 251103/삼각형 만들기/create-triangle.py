n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
def parallelx(i,j):
    x1, y1= points[i]
    x2, y2= points[j]
    if y1==y2:
        return abs(x1-x2)

def parallely(i,j):
    x1, y1= points[i]
    x2, y2= points[j]
    if x1==x2:
        return abs(y1-y2)
maxp=0
maxq=0
for i in range(n):
    maxa=0
    maxb=0
    for j in range(i+1,n):
        if parallelx(i,j):
            maxa=max(maxa, parallelx(i,j))
        elif parallely(i,j):
            maxb=max(maxb,parallely(i,j))
    maxp= max(maxp,maxa)
    maxq= max(maxq, maxb)
print(maxp*maxq)