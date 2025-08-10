a, b = map(int, input().split())

# Please write your code here.
def count(a,b):
    cnt=0

    for i in range(a,b+1):
        iscount=True
        if i%2==0:
            iscount= False
        elif i%10==5:
            iscount= False
        elif i%3==0 and i%9!=0:
            iscount= False
        
        if iscount:
            cnt+=1
    
    return cnt

print(count(a,b))

