n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)
#print(r,c)
# Please write your code here.
def in_range(x,y):
    return 0<=x < n and 0<=y<n

dirdict= {'U':0 , 'D':3 , 'R':1, 'L':2}
dxs,dys= [-1,0,0,1] , [0,1,-1,0]
x,y= r-1,c-1
#print(x,y)
cnt=0
dir_num=dirdict[d]
while cnt<=t:
    #print(f"dir_num: {dir_num}")
    nx, ny= x+dxs[dir_num] , y+dys[dir_num]
    #print(nx,ny)
    #print(in_range(nx,ny))
    if not in_range(nx,ny):
        dir_num= 3-dir_num
    x, y = x + dxs[dir_num], y + dys[dir_num]
    #print(nx,ny)
    #x,y=nx,ny
    cnt+=1
print(x+1,y+1)