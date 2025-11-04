n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)
# Please write your code here.

x=1 
while True:
    valid = True
    for i in range(n):
        temp=x*(2**(i+1))
        if temp< ranges[i][0] or temp>ranges[i][1]:
            valid=False
            break
    if valid:
        print(x)
        break
    x+=1



