n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
direction_map = {'N':0, 'E':1, 'S':2, 'W':3}

dx, dy= [0,1,0,-1] , [1,0,-1,0]
x,y=0,0
for d, dist in moves:
    idx = direction_map[d]
    nx,ny= x+ dx[idx]*int(dist) , y+ dy[idx]*int(dist)
    x,y= nx,ny
print(x,y)