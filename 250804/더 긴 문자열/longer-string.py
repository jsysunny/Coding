lista= list(map(str, input().split()))
if len(lista[0])== len(lista[1]):
    print("same")
elif len(lista[0])< len(lista[1]):
    print(f"{lista[1]} {len(lista[1])}")
elif len(lista[0])> len(lista[1]):
    print(f"{lista[0]} {len(lista[0])}")