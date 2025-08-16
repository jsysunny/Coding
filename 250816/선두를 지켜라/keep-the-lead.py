n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
posa=[0]*1000000; posb=[0]*1000000 ;
timea=1 ; timeb=1 ;
for i in range(n):
    for j in range(t[i]):
        #print(v[i])
        posa[timea]=posa[timea-1]+v[i]
        #print(posa[timea])
        timea+=1

for i in range(m):
    for j in range(t2[i]):
        posb[timeb]=posb[timeb-1]+v2[i]
        timeb+=1

#print(posa)
afirst=True

if posa[1]<posb[1]:
    afirst=False
#print(afirst)
cnt=0
for i in range(2,timea):
    if afirst and posa[i]<posb[i]:
        #print(1)
        afirst=False
        cnt+=1
    elif not afirst and posa[i]>posb[i]:
        #print(2)
        afirst=True
        cnt+=1
print(cnt)