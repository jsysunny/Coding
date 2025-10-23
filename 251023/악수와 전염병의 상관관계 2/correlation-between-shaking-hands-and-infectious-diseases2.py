N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.
handshakes1 = sorted(handshakes, key=lambda h: h[0])
#print(handshakes1)
# 원본 자체를 바꾸고 싶을때 handshakes.sort(key=lambda h: h[0])
cnt=0
posa=[0]*N

for h in handshakes1:
    #print(h[0],h[1],h[2])
    #print(P)
    if h[1] == P or h[2]==P:
        cnt+=1 
        if cnt<=K:
            posa[h[1]-1]=1
            posa[h[2]-1]=1 
        else:
            break

for i in range(N):
    print(posa[i],end="")

    