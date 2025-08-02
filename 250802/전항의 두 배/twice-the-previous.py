lista=list(map(int, input().split()))
for i in range(8):
    lista.append(lista[-1]+2*lista[-2])

for l in lista:
    print(l, end=" ")