n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
maxa=cnt=0
for i in range(n):
    if arr[i]>t:
        cnt+=1
    else:
        cnt=0
    maxa=max(maxa,cnt)
    #print(i,maxa,cnt)
print(maxa)