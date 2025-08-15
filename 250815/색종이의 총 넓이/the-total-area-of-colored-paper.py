n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

placed= [[0]*201 for _ in range(201)]
for i in range(n):
    for j in range(x[i],x[i]+8):
        for k in range( y[i], y[i]+8):
            placed[j][k]+=1

cnt=0
for i in range(201):
    for j in range(201):
        if placed[i][j]:
            cnt+=1
print(cnt)
# Please write your code here.