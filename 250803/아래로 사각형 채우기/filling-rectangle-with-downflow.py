n= int(input())

num=1
num1=1
lista= [ [0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        lista[i][j]=num1
        print(lista[i][j], end=" ")
        num1+=n
    num+=1
    num1=num
    print()

