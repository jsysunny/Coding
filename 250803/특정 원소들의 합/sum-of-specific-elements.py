lista= [list(map(int, input().split())) for _ in range(4)]
suma=0
for i in range(len(lista)):
    if i==0:
        suma+=lista[0][0]
    elif i==1:
        suma+=lista[1][0]+lista[1][1]
    elif i==2:
        suma+=lista[2][0]+lista[2][1]+lista[2][2]
    elif i==3:
        suma+=lista[3][0]+lista[3][1]+lista[3][2]+lista[3][3]

print(suma)