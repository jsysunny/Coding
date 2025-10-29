n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
maxcnt=0
for i in range(n):
    for j in range(n-2):
        maxcnt= max(maxcnt, grid[i][j]+grid[i][j+1]+grid[i][j+2])
print(maxcnt)