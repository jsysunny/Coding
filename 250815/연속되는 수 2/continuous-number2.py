n = int(input())
arr = [int(input()) for _ in range(n)]

cnt=maxa=0
# Please write your code here.
for i in range(n):
    if i>=1 and arr[i]==arr[i-1]:
        cnt+=1
    else:
        cnt=1
    maxa=max(maxa,cnt)
print(maxa)