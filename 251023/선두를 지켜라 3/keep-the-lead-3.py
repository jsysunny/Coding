N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
T=max(sum(t), sum(t2))
#print(T)
posa=[0]*(T+1) ; posb=[0]*(T+1)
timea=1 ; timeb=1;


for i in range(N):
    for j in range(t[i]):
        posa[timea]= posa[timea-1]+ v[i]
        timea+=1 

for i in range(M):
    for j in range(t2[i]):
        posb[timeb]= posb[timeb-1]+ v2[i]
        timeb+=1 

first=0
if posa[1] < posb[1]:
    first = 1
elif posa[1] > posb[1]:
    first =2

cnt=1
for i in range(2,timea):
    if first==1 and posa[i]>= posb[i]:
        cnt+=1
        first==2 if posa[i]>posb[i] else 0
    elif first==2 and posa[i]<= posb[i]:
        cnt+=1
        first==1 if posa[i]<posb[i] else 0
    elif first==0 and posa[i]!=posb[i]:
        cnt+=1
        first==1 if posa[i]<posb[i] else 2

print(cnt)


