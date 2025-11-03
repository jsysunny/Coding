n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

mind=float("inf")
# Please write your code here.
for i in range(n):
    for j in range(i+1,n):
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        dist = dx * dx + dy * dy
        mind = min(mind, dist)

print(mind)
