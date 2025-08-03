lista= [ [0 for _ in range(5)] for _ in range(5)]
for j in range(5):
    lista[0][j]=1

for i in range(5):
    lista[i][0]=1

for i in range(1,5):
    for j in range(1,5):
        lista[i][j]= lista[i-1][j] + lista[i][j-1]

for i in range(5):
    for j in range(5):
        print(lista[i][j], end= " ")
    print() 