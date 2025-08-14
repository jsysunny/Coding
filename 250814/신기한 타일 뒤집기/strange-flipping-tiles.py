n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
segments=[]
cur=0 ; left=0 ; right=0
for i in range(len(dir)):
    if dir[i]=="L":
        left=cur- x[i]
        right=cur
        cur-=x[i]
        segments.append([left,right, "L"])
    
    else:
        left=cur
        right=cur+x[i]
        cur+=x[i]
        segments.append([left, right, "R"])
#print(segments)
placed=[0]*20000
for s in segments:
    for i in range(s[0],s[1]):
        placed[i]=s[2]

cntl=cntr=0
for i in range(20000):
    if placed[i]=="L":
        cntl+=1
    elif placed[i]=="R":
        cntr+=1

print(cntl,cntr)