
lista = [list(map(int, input().split())) for _ in range(3)]
input()
listb = [list(map(int, input().split())) for _ in range(3)]


for i in range(3):
    for j in range(3):
        print(lista[i][j] * listb[i][j], end=" ")
    print()
