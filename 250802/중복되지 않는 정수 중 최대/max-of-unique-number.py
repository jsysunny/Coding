n = int(input())
nums = list(map(int, input().split()))

new=[]
# Please write your code here.
for n in nums:
    if nums.count(n)==1:
        new.append(n)

if new:
    print(max(new))
else:
    print(-1)