n = int(input())
A = list(map(int, input().split()))

# Please write your code here.

suma=0 
summin=10000
for i in range(len(A)):
    for j in range(len(A)):
        suma+= abs(j-i)*A[j]
    summin= min( suma,summin )
    #print(suma)
    #print(summin)
    suma=0
    
print(summin)