N = int(input())

# Please write your code here.
def suma(N):
    if N==1:
        return 1
    return suma(N-1)+N

print(suma(N))

