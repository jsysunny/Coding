n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

max_area2 = 0  # 넓이의 2배

for i in range(n):
    x1, y1 = points[i]
    max_x = 0
    max_y = 0

    for j in range(n):
        if i == j:
            continue
        x2, y2 = points[j]
        if y1 == y2:  # 가로선 조건
            max_x = max(max_x, abs(x1 - x2))
        if x1 == x2:  # 세로선 조건
            max_y = max(max_y, abs(y1 - y2))

    # 기준점 i에서 가로, 세로 모두 가능해야 삼각형 가능
    area2 = max_x * max_y
    max_area2 = max(max_area2, area2)

print(max_area2)

# Please write your code here.
# 삼각형을 만들려면 한 점을 기준으로 해야 하기 때문에 틀림 
"""
def parallelx(i,j):
    x1, y1= points[i]
    x2, y2= points[j]
    if y1==y2:
        return abs(x1-x2)
    return None

def parallely(i,j):
    x1, y1= points[i]
    x2, y2= points[j]
    if x1==x2:
        return abs(y1-y2)
    return None
maxp=0
maxq=0
for i in range(n):
    maxa=0
    maxb=0
    for j in range(i+1,n):
        #print(parallelx(i, j))
        #print(parallely(i, j))
        if parallelx(i,j) is not None:
            maxa=max(maxa, parallelx(i,j))
        if parallely(i,j) is not None:
            maxb=max(maxb,parallely(i,j))
    maxp= max(maxp,maxa)
    maxq= max(maxq, maxb)
print(maxp*maxq)
"""