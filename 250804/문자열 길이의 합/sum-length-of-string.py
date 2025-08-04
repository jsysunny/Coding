n = int(input())
lena=0
cnt=0
for _ in range(n):
    str=input()
    lena+=len(str)
    if str[0]=='a':
        cnt+=1

print(lena, cnt)