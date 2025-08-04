n=int(input())
lista=[]
for _ in range(n):
    str=input()
    lista.append(str)

cnt=0
lena=0
for l in lista:
    if l[0]=='c':
        cnt+=1
        lena+=len(l)

print(f"{cnt} {lena/cnt:0.2f}")