a,b = map(int, input().split())
cnt=[0]*9
while a>1:
    c=a%b
    cnt[c]+=1
    a=a//b


suma=0
for c in cnt:
    suma+=c**2

print(suma)