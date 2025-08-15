n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
placed=[[0]*201 for _ in range(201)]
for i in range(n):
    for j in range(x1[i]+100, x2[i]+100):
        for k in range(y1[i]+100,y2[i]+100):
            if i%2==0:
                placed[j][k]=1
            else:
                placed[j][k]=-1

cnt=0
for i in range(201):
    for j in range(201):
        if placed[i][j]==-1:
            cnt+=1
print(cnt)

