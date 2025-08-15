x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
placed=[ [0]*2001 for _ in range(2001)]
for k in range(len(x1)):
    for i in range(x1[k],x2[k]):
        for j in range(y1[k], y2[k]):
            if k==0:
                placed[i][j]+=1
            else:
                placed[i][j]-=1

cnt=[]
height=width=0
for i in range(x1[0],x2[0]):
    cnt1=0
    for j in range(y1[0],y2[0]):
        if placed[i][j]:
            cnt1+=1
    if cnt1>0:
        height= max(height, cnt1)
cnt.append(height)


for j in range(y1[0],y2[0]):
    cnt2=0
    for i in range(x1[0],x2[0]):
        if placed[i][j]:
            cnt2+=1
    if cnt2>0:
        width=max(width,cnt2)
cnt.append(width)

if cnt[0]==0 and cnt[1]==0:
    print(0)
else:
    print(cnt[0]*cnt[1])

        