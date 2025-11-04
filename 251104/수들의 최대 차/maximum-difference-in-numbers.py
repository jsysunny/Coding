N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
minc=float("inf")
for i in range(10000):
    cost=0
    for a in arr:
        if a>=i and a<=i+2:
            continue
        elif a<i:
            cost+= i-a
        else:
            cost+= a-(i+2)
    minc= min(minc, cost)
print(minc)