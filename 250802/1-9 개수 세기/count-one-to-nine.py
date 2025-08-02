n= int(input())
lista= list(map(int, input().split()))

count=[0]*9
for i in range(1,10):
    for l in lista:
        if l==i:
            count[i-1]+=1

for c in count:
    print(c)