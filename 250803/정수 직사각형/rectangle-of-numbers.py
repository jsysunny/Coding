n,m= map(int, input().split())

num=1
arr2d=[ [0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        arr2d[i][j]= num
        num+=1
        print(arr2d[i][j], end=" ")
    print()