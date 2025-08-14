n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
placed= [0]*n
for c in commands:
    for i in range(c[0]-1, c[1]):
        placed[i]+=1

print(max(placed))