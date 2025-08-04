n,m = map(int, input().split())
placed= [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r,c= map(int, input().split())
    placed[r-1][c-1]=r*c

for i in range(n):
    for j in range(n):
        print(placed[i][j], end= " ")
    print()