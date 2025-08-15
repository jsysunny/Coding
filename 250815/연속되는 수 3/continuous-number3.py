N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

cnt=maxa=1
for i in range(N):
    if i>=1 and arr[i]*arr[i-1]>0:
        cnt+=1
    else:
        cnt=1
    maxa=max(maxa,cnt)
print(maxa)