n, m = map(int, input().split())

lista =[ [0 for _ in range(m)] for _ in range(n)]
# Please write your code here.
num=0
for j in range(m):
    if j%2==0:
        for i in range(n):
            lista[i][j]=num
            num+=1
    else:
        for i in range(n-1,-1,-1):
            lista[i][j]=num
            num+=1
    

for i in range(n):
    for j in range(m):
        print(lista[i][j], end=" ")
    print()