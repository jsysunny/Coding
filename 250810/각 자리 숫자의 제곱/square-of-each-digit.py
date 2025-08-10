N = int(input())

# Please write your code here.
def suma(N):
    if N<10:
        return N**2
    return suma(N//10) + (N%10)**2

print(suma(N))