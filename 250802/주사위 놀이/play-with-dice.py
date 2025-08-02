lista= list(map(int, input().split()))

count=[0 for _ in range(7)]
for l in lista:
    count[l]+=1

for i in range(1,len(count)):
    print(f"{i} - {count[i]}")