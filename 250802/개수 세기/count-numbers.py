a,b = tuple(map(int,input().split()))

lista=list(map(int, input().split()))

if b in lista:
    print(lista.count(b))