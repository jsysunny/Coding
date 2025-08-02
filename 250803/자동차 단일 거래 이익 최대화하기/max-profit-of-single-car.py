n = int(input())
price = list(map(int, input().split()))

new=[]
# Please write your code here.
for i in range(n):
    for j in range(i+1,n):
        new.append(price[i]-price[j])

new=[x for x in new if x<0]

if new:
    print(-min(new))
else:
    print(0)
