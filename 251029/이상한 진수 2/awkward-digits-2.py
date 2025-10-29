a = input()
a=list(a)
# Please write your code here.

for i in range(len(a)):
    if a[i]=='0':
        a[i]='1'
        break

suma=0
for i in range(len(a)):
    #print(int(a[i]))
    suma += 2**(len(a)-1-i) * int(a[i])
    #print("합",2**(len(a)-1-i))
print(suma)