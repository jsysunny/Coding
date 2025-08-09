n = int(input())

# Please write your code here.
def splita(n):
    suma=0
    for i in range(1,n+1):
        suma+=i
    return suma//10

print(splita(n))