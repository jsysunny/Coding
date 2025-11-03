X, Y = map(int, input().split())

# Please write your code here.
maxa=0
for i in range(X,Y+1):
    i=str(i)
    #print(i[0])
    maxa=max(maxa, int(i[0])+int(i[1]))
print(maxa)
    

