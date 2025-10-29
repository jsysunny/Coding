n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
final=float('inf')
for i in range(1,len(points)-1):
    suma=0
    for j in range(1,len(points)):
        if j==i :
            continue
        elif j==i+1:
            suma+=abs(points[j][0]- points[j-2][0])+abs(points[j][1]- points[j-2][1])
            #print(i,suma)
        else:
            suma+=abs(points[j][0]- points[j-1][0])+abs(points[j][1]- points[j-1][1])
            #print(i,suma)
    final = min(suma, final)

print(final)