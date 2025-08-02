n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
mina=a[0]
for i in range(1,len(a)):
    if mina > a[i]:
        mina=a[i]

print(f"{mina} {a.count(mina)}")