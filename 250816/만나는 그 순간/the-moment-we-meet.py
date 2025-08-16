n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

#print(d)
#print(t)
posa=[0]*1000000
posb=[0]*1000000
# Please write your code here.
timea=1
for i in range(n):
    if d[i]=="R":
        for k in range(t[i]):
            #print(t[i])
            posa[timea]=posa[timea-1]+1
            #print(posa[timea])
            timea+=1
            
    else:
        for k in range(t[i]):
            posa[timea]=posa[timea-1]-1
            timea+=1

timeb=1
for i in range(m):
    if d2[i]=="R":
        for k in range(t2[i]):
            #print(t[i])
            posb[timeb]=posb[timeb-1]+1
            #print(posa[timea])
            timeb+=1
            
    else:
        for k in range(t2[i]):
            posb[timeb]=posb[timeb-1]-1
            timeb+=1
#print(timeb, posb)
ans=-1
for i in range(1,timea):
    if posa[i]==posb[i]:
        ans=i
        break
print(ans)

