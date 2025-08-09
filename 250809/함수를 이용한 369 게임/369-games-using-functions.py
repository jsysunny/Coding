a, b = map(int, input().split())

# Please write your code here.
def A(a,b):
    cnt=0
    for i in range(a,b+1):
        if i%3==0:
            cnt+=1
            continue
        i=str(i)
        for j in range(len(i)):
            if i[j]=='3' or i[j]=='6' or i[j]=='9':
                cnt+=1
                break
    return cnt

print(A(a,b))
