a, b = map(int, input().split())
lista = list(map(int, input().split()))
listb = list(map(int, input().split()))

found = False

for i in range(a - b + 1):  
    if lista[i:i + b] == listb:
        found = True
        break

print("Yes" if found else "No")
