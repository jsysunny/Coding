lista= list(map(int, input().split()))

cnt=[0 for _ in range(11)]
for i in range(1,11):
    for l in lista:
        if l<10:
            continue
        elif l//10==i:
            cnt[i]+=1


for n in range(10,0,-1):
    print(f"{n}0 - {cnt[n]}")