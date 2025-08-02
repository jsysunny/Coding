n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
for n in nums:
    if nums.count(n)>=2:
        for _ in range(nums.count(n)):
            nums.remove(n)

if nums:
    print(max(nums))
else:
    print(-1)