n, q= tuple(map(int, input().split()))

lista=list(map(int, input().split()))

for _ in range(q):
    listb =list(map(int, input().split()))
    if listb[0]==1:
        print(lista[listb[1]-1])
    elif listb[0]==2:
        if listb[1] in lista:
            print(lista.index(listb[1])+1)
            continue
        else:
            print(0)
    elif listb[0]==3:
        for i in range(listb[1]-1, listb[2]):
            print(lista[i], end=" ")
        print()