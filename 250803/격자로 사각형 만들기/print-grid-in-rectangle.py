n=int(input())
lista= [ [0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    lista[i][0]=1

for j in range(n):
    lista[0][j]=1

for i in range(1,n):
    for j in range(1,n):
        lista[i][j]= lista[i-1][j-1]+ lista[i-1][j]+lista[i][j-1]

for i in range(n):
    for j in range(n):
        print(lista[i][j], end=" ")
    print()