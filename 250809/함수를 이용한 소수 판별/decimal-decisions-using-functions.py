a, b = map(int, input().split())

# Please write your code here.]
def prime(a,b):
    cnt=0
    suma=0
    for i in range(a,b+1):
        isprime=True
        for j in range(2,i):
            if i%j==0:
                isprime=False
                break
        if isprime:
            suma+=i
    
    return suma

print(prime(a,b))