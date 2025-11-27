n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n-1):
    mina=i
    for j in range(i+1,n):
        if arr[j]< arr[mina]:
            mina=j
    arr[i],arr[mina]= arr[mina],arr[i]

for a in arr:
    print(a, end=" ")