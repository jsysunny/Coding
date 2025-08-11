n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
new=[]
for s in str:
    if s[:len(t)]==t:
        new.append(s)

new.sort()
print(new[k-1])    