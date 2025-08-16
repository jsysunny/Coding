dirs = input()

# Please write your code here.

dx, dy= [0,1,0,-1], [1,0,-1,0]

dirnum1=0
x,y=(0,0)
for dir in dirs:
    if dir=='L':
        dirnum1= (dirnum1+3)%4
    elif dir=='R':
        dirnum1= (dirnum1+1)%4
    elif dir== 'F':
        nx, ny= x+dx[dirnum1], y+dy[dirnum1]
        x,y=nx,ny
print(x,y)
