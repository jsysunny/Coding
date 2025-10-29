n, k = map(int, input().split())
arr = list(map(int, input().split()))

maxa=0
# Please write your code here.
for i in range(n-k+1):
    suma=0
    for j in range(i, i+k):
        suma+=arr[j]
    maxa= max(maxa, suma)
print(maxa)