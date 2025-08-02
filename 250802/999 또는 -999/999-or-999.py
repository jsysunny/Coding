lista=[]
while True:
    list1=list(map(int, input().split()))
    if not list1:
        continue
    if list1[-1]==999 or list1[-1]==-999:
        lista=list1[:-1]
        break
    
    #print(lista)

print(f"{max(lista)} {min(lista)}")
