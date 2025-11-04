N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
maxc=0
for i in range(10000):
    cost=0
    for a in arr:
        if a>=i and a<=i+K:
            cost+=1
    maxc= max(maxc, cost)
print(maxc)