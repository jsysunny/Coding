n=int(input())
lista= list(map(int, input().split()))

mina=99
for i in range(n):
    for j in range(i+1,n):
        dif= abs(lista[i]-lista[j])
        if dif <mina:
            mina=dif

print(mina)