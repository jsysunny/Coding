N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
for i in range(N):
    arr[i]=str(arr[i])

cnt=maxa=0
for i in range(N):
    if i>=1 and len(arr[i])==len(arr[i-1]):
        cnt+=1
    else:
        cnt=1
    #print(maxa)
    maxa=max(maxa,cnt)
print(maxa)