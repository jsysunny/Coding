n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


cnt = 0
sum=0
for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = i+ dx, j+dy
            if in_range(nx, ny) and grid[nx][ny] == 1:
                cnt += 1
        if cnt>=3:
            sum+=1

print(sum)


