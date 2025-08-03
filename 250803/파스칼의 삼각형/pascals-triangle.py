n= int(input())
lista= [ [0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    lista[i][0]=1

for i in range(n):
    for j in range(n):
        if i==j:
            lista[i][j]=1

for i in range(2,n):
    for j in range(1,i):
        lista[i][j]=lista[i-1][j-1]+ lista[i-1][j]

for i in range(n):
    for j in range(i+1):
        print(lista[i][j], end=" ")
    print()