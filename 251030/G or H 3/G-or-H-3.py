n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

posa=[0]*10001
posb=[0]*10001
# Please write your code here.
for i in range(k):
    posa[x[i]]=1
    posb[x[i]]=c[i]


maxa=0
for i in range(10000-k+1):
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
        else:
            continue
    maxa= max(maxa,suma)
print(maxa)
        