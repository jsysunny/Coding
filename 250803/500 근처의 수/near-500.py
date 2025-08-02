lista=list(map(int, input().split()))
newa=[]
newb=[]
for a in lista:
    if a<500:
        newa.append(a)
    elif a>500:
        newb.append(a)

print(f"{max(newa)} {min(newb)}") 