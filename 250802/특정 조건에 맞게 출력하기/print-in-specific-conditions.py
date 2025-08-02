lista= list(map(int, input().split()))
new=[]
for l in lista:
    if l ==0:
        break
    elif l%2==0:
        new.append(l//2)
    else:
        new.append(l+3)

for n in new:
    print(n, end=" ")