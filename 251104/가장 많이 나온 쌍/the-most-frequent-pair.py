n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
maxa=0
for i in range(m):
    x,y =pairs[i]
    cnt=0
    for j in range(i,m):
        x1,y1=pairs[j]
        if x1==x and y1==y or x1==y and y1==x:
            cnt+=1
    maxa= max(maxa, cnt)
print(maxa)