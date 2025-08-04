stra=input()
n=int(input())
n = min(n, len(stra))
for i in range(len(stra)-1,len(stra)-n-1,-1):
    print(stra[i], end="")