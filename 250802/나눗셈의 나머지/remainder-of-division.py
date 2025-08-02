a,b = map(int, input().split())
cnt=[0]*b
while a>1:
    c=a%b
    #print(c)
    cnt[c]+=1
    #print(cnt)
    a=a//b


suma=0
for c in cnt:
    #print(c)
    suma+=c**2
    #print(suma)

print(suma)