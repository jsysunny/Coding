n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
right=cnt=maxa=0
new=[]
for right in range(len(arr)):
    while arr[right] in new:
        new.remove(arr[right])
        cnt+=1
        maxa=max(maxa,cnt)
    new.append(arr[right])
    #rint(new)
print(maxa)