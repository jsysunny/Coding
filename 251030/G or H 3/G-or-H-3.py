n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

#print(max(x))
posa=[0]*(max(x)+1)
posb=[0]*(max(x)+1)
# Please write your code here.

for i in range(len(x)):
    posa[x[i]]=1
    posb[x[i]]=c[i]


maxa=0
for i in range(1,max(x)-k+1):
    suma=0
    for j in range(i,i+k+1):
        if posa[j]==1:
            if posb[j]=="G":
                suma+=1
                #print(i,j,suma)
            elif posb[j]=="H":
                suma+=2
                #print(i,j,suma)
        else:
            continue
    maxa= max(maxa,suma)
print(maxa)
