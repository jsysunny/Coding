N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]




def a(num,Ta,Tb,C,H,G):
    if num <Ta :
        return C
    elif num <= Tb:
        return G
    else:
        return H

maxa=0
for num in range(0,1001):
    suma=0
    for i in range(N):
        Ta,Tb=ranges[i]
        suma+= a(num,Ta,Tb,C,H,G)
    maxa=max(maxa,suma)


print(maxa)

