n = int(input())
A = list(map(int, input().split()))

# Please write your code here.

suma=0 
summin= float('inf') 
for i in range(len(A)):
    suma=0
    for j in range(len(A)):
        suma+= abs(j-i)*A[j]
    summin= min( suma,summin )
    #print(suma)
    #print(summin)

    
print(summin)