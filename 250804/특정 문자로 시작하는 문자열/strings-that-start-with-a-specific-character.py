n=int(input())
lista=[]
for _ in range(n):
    str=input()
    lista.append(str)
str1=input()
cnt=0
lena=0
for l in lista:
    if l[0]==str1:
        cnt+=1
        lena+=len(l)

print(f"{cnt} {lena/cnt:0.2f}")