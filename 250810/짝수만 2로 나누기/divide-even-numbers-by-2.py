n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def rewrite(arr):
    for i in range(n):
        if arr[i]%2==0:
            arr[i]=arr[i]//2
    return arr

for j in rewrite(arr):
    print(j, end=" ")