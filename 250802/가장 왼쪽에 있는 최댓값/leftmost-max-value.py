n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
while True:
    idx= a.index(max(a))
    print(idx+1, end=" ")
    if idx==0:
        break
    a=a[:idx]