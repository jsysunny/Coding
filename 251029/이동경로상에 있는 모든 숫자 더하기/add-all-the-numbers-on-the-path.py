N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
x,y = N//2, N//2 
dir_num=3 
def in_range(x,y):
    return 0<=x and x<N and 0<=y and y<N

dxs, dys = [0,1,0,-1] , [1,0,-1,0]

sum=board[x][y]
for s in str:
    if s=="L":
        dir_num = (dir_num+3)%4
    elif s=="R":
        dir_num = (dir_num+1)%4
    else:
        nx, ny= x+ dxs[dir_num] , y+ dys[dir_num]
        if in_range(nx,ny):
            x,y = x+ dxs[dir_num] , y+ dys[dir_num]
            sum += board[x][y]
        else:
            continue
print(sum)