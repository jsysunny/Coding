n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

segments=[]
cur=0 ; right=0; left=0;
# Please write your code here.
for i in range(len(dir)):
    if dir[i]=="L":
        
        left= cur-int(x[i])
        right=cur
        cur-=int(x[i])
        #print(cur)
    else:
        
        left=cur
        right=cur+int(x[i])
        cur+=int(x[i])
        #print(cur)
    segments.append([left, right])

#print(segments)
placed=[]
for s in segments:
    for i in range(s[0],s[1]):
        placed.append(i)
#print(placed)
cnt=0
for p in set(placed):
    if placed.count(p)>=2:
        #print(p)
        cnt+=1
print(cnt)



