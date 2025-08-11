n, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
for i,e in enumerate(nums):
    if i==k-1:
        print(e)