n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
new=[]
nums.sort()
for i in range(n):
    new.append(nums[i]+nums[2*n-i-1])

new.sort(reverse=True)
print(new[0])