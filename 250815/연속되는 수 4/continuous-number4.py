n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cnt=maxa=0
for i in range(n):
    if i>=1 and arr[i]>=arr[i-1]:
        cnt+=1
    else:
        cnt=0
    maxa=max(maxa,cnt)
print(maxa)