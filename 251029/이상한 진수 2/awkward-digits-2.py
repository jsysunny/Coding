a = input()
a=list(a)
# Please write your code here.
flag= False
for i in range(len(a)):
    if a[i]=='0':
        flag=True
        a[i]='1'
        break
if not flag:
    a[len(a)-1]='0'

suma=0
for i in range(len(a)):
    #print(int(a[i]))
    suma += 2**(len(a)-1-i) * int(a[i])
    #print("합",2**(len(a)-1-i))
print(suma)

# 이진수 → 10진수 변환
#ans = int(''.join(a), 2)
#print(ans)