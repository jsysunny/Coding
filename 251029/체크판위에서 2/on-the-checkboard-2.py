R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

count=0
# Please write your code here.
#print(grid[0][0])
for i1 in range(R):
    for j1 in range(C):
        # 두 번째 점프: (i2, j2) > (i1, j1)
        for i2 in range(i1 + 1, R):
            for j2 in range(j1 + 1, C):
                # 색이 달라야 점프 가능
                for i3 in range(i2 + 1, R):
                    for j3 in range(j2 + 1, C):
                        if grid[0][0] != grid[i1][j1] and grid[i1][j1] != grid[i2][j2] and grid[i2][j2]!=grid[i3][j3]:
                        # 마지막 위치가 도착지인지 확인
                            #print(grid[i1][j1])
                            #print(i1,j1)
                            #print(grid[i2][j2])
                            #print(i2, j2)
                            if i3 == R - 1 and j3 == C - 1:
                                count += 1
print(count)