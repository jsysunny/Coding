commands = input()

x,y=0,0
curr_dir=3
dxs= [1,0,-1 ,0]
dys= [0, -1 ,0,1]

flag =False

leng= len(commands)

for i in range(leng):
    cdir=commands[i]
    if cdir=='L':
        curr_dir= (curr_dir+3)%4
    elif cdir=="R":
        curr_dir= (curr_dir+1)%4
    else:
        x,y= x+dxs[curr_dir], y+dys[curr_dir]
    
    if x==0 and y==0:
        print(i+1)
        flag=True
        break
        
if flag==False:
    print(-1)