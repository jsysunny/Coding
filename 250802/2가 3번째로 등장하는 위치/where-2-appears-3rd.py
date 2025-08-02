n=int(input())

lista=list(map(int, input().split()))

count=0
for i in range(len(lista)):
    if lista[i]==2:
        count+=1
        if count ==3:
            print(i+1)