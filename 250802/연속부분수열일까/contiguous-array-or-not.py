a, b = map(int, input().split())
lista = list(map(int, input().split()))
listb = list(map(int, input().split()))

idx = 0  

for val in lista:
    if val == listb[idx]:
        idx += 1
        if idx == b:  
            break

print("Yes" if idx == b else "No")
