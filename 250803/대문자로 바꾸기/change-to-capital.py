for _ in range(5):

    lista = list(map(str, input().split()))

    for i in range(len(lista)):
        lista[i]=lista[i].upper()
    
    print(' '.join(lista))