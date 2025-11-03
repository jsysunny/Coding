n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

minc=float("inf")
mind=float("inf")
# Please write your code here.
for i in range(n):
    mina=float("inf")
    minb=float("inf")
    for j in range(i+1,n):
        mina= min (mina, abs(points[i][0]- points[j][0]))
        minb= min (minb, abs(points[i][1]- points[j][1]))
    minc= min(minc,mina)
    mind= min(mind,minb)

print(minc**2+ mind**2)
