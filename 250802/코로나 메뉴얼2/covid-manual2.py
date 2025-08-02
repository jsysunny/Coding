cnt=[0]*4
sys=[]
for _ in range(3):
    lista=list(map(str, input().split()))
    if lista[0]=='Y' and int(lista[1])>=37:
        sys.append('A')
    elif lista[0]=='N' and int(lista[1])>=37:
        sys.append('B')
    elif lista[0]=='Y' and int(lista[1])<37:
        sys.append('C')
    else:
        sys.append('D')

for s in sys:
    idx=ord(s)-ord('A')
    cnt[idx]+=1


for c in cnt:
    print(c, end=" ")
if cnt[0]>=2:
    print('E')

