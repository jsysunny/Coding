n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
placed=[]
for s in segments:
    for i in range(s[0],s[1]+1):
        placed.append(i)

counted=[]
for p in set(placed):
    counted.append(placed.count(p))

print(max(counted))