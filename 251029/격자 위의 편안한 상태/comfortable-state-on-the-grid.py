n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

grid = [[0]*n for _ in range(n)]

dxs, dys = [1,0,-1,0], [0,1,0,-1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for x, y in points:
    x -= 1
    y -= 1
    grid[x][y] = 1

    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] == 1:
            cnt += 1

    if cnt == 3:
        print(1)
    else:
        print(0)
