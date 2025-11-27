n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n-1):
    for j in range(n-1-i):
        if arr[j]>arr[j+1]:
            temp= arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp

for a in arr:
    print(a,end=" ")