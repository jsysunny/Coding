n= int(input())

lista= [[0 for _ in range(n)] for _ in range(n)]

num=1
if n%2==0:
    for j in range(n-1,-1, -1):
        if j%2!=0:
            for i in range(n-1,-1,-1):
                lista[i][j]=num
                num+=1
        else:
            for i in range(n):
                lista[i][j]=num
                num+=1
else:
    for j in range(n-1,-1, -1):
        if j%2==0:
            for i in range(n-1,-1,-1):
                lista[i][j]=num
                num+=1
        else:
            for i in range(n):
                lista[i][j]=num
                num+=1


for i in range(n):
    for j in range(n):
        print(lista[i][j], end=" ")
    print()