n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
a.sort()
#print(a)

print(f"{a[-1]} {a[-2]}")