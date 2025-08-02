lista= list(map(int, input().split()))

new=[]
for l in lista:
    if l==0:
        break
    new.append(l)

cnt=[0 for _ in range(9)]
for n in new:
    if n//10==0:
        continue
    else:
        cnt[n//10-1]+=1


for i in range(1,10):
    print(f"{i} - {cnt[i-1]}")