x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
offset=1000
max_offset=2000
placed= [ [0]*(max_offset+1) for _ in range(max_offset+1)]

for i in range(len(x1)):
    for j in range(x1[i]+offset, x2[i]+offset):
        for k in range(y1[i]+offset,y2[i]+offset):
            if i!=2:
                placed[j][k]+=1
            else:
                if placed[j][k]:
                    placed[j][k]-=1

cnt=0
for i in range(max_offset+1):
    for j in range(max_offset+1):
        if placed[i][j]:
            cnt+=1
print(cnt)