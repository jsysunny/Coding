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
for i in range(x1[0],x2[0]):
    cnt1=0
    for j in range(y1[0],y2[0]):
        if placed[i][j]:
            cnt1+=1
    if cnt1==y2[0]-y1[0]:
        cnt.append(cnt1)
        break
if not cnt:
    cnt.append(cnt1)

for j in range(y1[0],y2[0]):
    cnt2=0
    for i in range(x1[0],x2[0]):
        if placed[i][j]:
            cnt2+=1
    if cnt2==x2[0]-x1[0]:
        cnt.append(cnt2)
        break
if len(cnt)==1:
    cnt.append(cnt2)

print(cnt[0]*cnt[1])

        