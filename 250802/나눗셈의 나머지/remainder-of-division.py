a,b = map(int, input().split())
cnt=[0]*9
while a>1:
    a=a//b
    c=a%b
    cnt[c]+=1

suma=0
for c in cnt:
    suma+=c**2

print(suma)