str=input()
n=int(input())
for i in range(len(str)-1,len(str)-n-1,-1):
    print(str[i], end="")