n,m= map(int, input().split())
lista= [ list(map(int, input().split())) for _ in range(n)]
listb= [ list(map(int, input().split())) for _ in range(n)]

listc= [ [0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if lista[i][j]== listb[i][j]:
            listc[i][j]=0
        else:
            listc[i][j]=1

for i in range(n):
    for j in range(m):
        print(listc[i][j], end=" ")
    print()
