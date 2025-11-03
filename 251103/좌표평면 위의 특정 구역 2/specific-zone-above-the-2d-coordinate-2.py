n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

minp=float("inf")
for i in range(n):
    minax=40000
    maxax=0
    minay=40000
    maxay=0
    for j in range(n):

        if j==i:
            continue
        x1,y1= points[j]
        minax=min(minax, x1)
        #print("1",minax)
        maxax =max(maxax,x1)
        #print("2",maxax)
        minay=min(minay, y1)
        #print("3",minay)
        maxay =max(maxay,y1)
        #print("4",maxay)
    minp=min(minp, (maxax-minax)*(maxay-minay))

print(minp) 

