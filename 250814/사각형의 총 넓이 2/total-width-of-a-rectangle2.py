n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
placed = [ [0]*201 for _ in range(201)]
for i in range(len(x1)):
    for j in range(x1[i], x2[i]):
        for k in range(y1[i],y2[i]):
            placed[j][k]+=1

cnt=0
for i in range(201):
    for j in range(201):
        if placed[i][j]:
            cnt+=1
print(cnt)