n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
mina=float("inf")
for i in range(n):
    arr[i]*=2
    for j in range(n):
        remain=[]
        for k in range(n):
            if k!=j:
                remain.append(arr[k])
        sumd=0
        for k in range(n-2):
            sumd += abs(remain[k+1]- remain[k])
        mina=min(mina,sumd)
    arr[i]//=2
print(mina)