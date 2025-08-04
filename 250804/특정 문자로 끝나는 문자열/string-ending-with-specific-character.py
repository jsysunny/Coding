lista=[]
for _ in range(10):
    lista.append (input())
str1=input()
cnt=0
for l in lista:
    if l[-1]==str1:
        print(l)
        cnt+=1
if cnt==0:
    print("None")
