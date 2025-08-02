n = int(input())
price = list(map(int, input().split()))

new=[]
# Please write your code here.
for i in range(n):
    for j in range(i+1,n):
        new.append(price[i]-price[j])

if min(new)<0:
    print(-min(new))
else:
    print(0)