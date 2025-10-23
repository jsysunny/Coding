n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.

TA = sum(t)       # A의 총 이동초
TB = sum(t_b)     # B의 총 이동초
T  = max(TA, TB)

posa = [0] * (T + 1)
posb = [0] * (T + 1)

timea=1 ; timeb=1 ;
for i in range(n):
    for j in range(t[i]):
        posa[timea]=posa[timea-1]+(1 if d[i]=="R" else -1)
        timea+=1
        
for i in range(timea,T+1):
    posa[i]=posa[timea-1]

for i in range(m):
    for j in range(t_b[i]):
        posb[timeb]=posb[timeb-1]+(1 if d_b[i]=="R" else -1)
        timeb+=1

for i in range(timeb,T+1):
    posb[i]=posb[timeb-1]

#print(posa)
ans=0
for i in range(1,T+1):
    if posa[i-1]!= posb[i-1] and posa[i]==posb[i]:
        ans+=1
        #print(i)
#print(posa[12], posb[12])
#print(posa[13], posb[13])
print(ans)