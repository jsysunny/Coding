X, Y = map(int, input().split())

# Please write your code here.
maxa=0
for i in range(X,Y+1):
    i=str(i)
    #print(i[0])
    suma=0
    for k in range(len(i)):
        suma+=int(i[k])
    maxa=max(maxa, suma)
print(maxa)
    

