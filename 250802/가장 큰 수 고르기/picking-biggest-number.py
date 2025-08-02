lista = list(map(int, input().split()))

maxa=lista[0]
for i in range(1,len(lista)):
    if lista[i]> maxa:
        maxa= lista[i]

print(maxa)