n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums1=nums[:]
nums1.sort()
for n in nums1:
    print(n, end= " ")
print()

nums.sort(reverse= True)
for n in nums:
    print(n, end= " ")