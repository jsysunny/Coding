N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
x,y=0,0
dirdist= { 'N' :0 , 'E':1, 'S':2, 'W':3}
dxs, dys= [-1, 0, 1,0], [0,1,0,-1]

cnt=0
for dir, dist in moves:
    dir_num=dirdist[dir]
    #print(int(dist))
    for i in range(int(dist)):  
        x,y= x+ dxs[dir_num], y+dys[dir_num]
        cnt+=1
        #print(x,y)
       
        if x== 0 and y==0:
            print(cnt)
            exit()
        #print(cnt)
if cnt==0:
    print(-1)