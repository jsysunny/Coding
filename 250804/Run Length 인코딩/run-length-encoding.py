A = input()
count=0
lista=[]
# Please write your code here.
for i in range(len(A)-1):
    if A[i]==A[i+1]:
        count+=1
    else:
        lista.append(A[i])
        lista.append(str(count+1))
        count=0

lena=0
lista.append(A[-1])
lista.append(str(count + 1))

for i in lista:
    lena+=len(i)

print(lena)
for i in lista:
    print(i, end="")