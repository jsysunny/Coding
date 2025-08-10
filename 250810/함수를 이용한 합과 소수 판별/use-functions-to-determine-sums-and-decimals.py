a, b = map(int, input().split())

# Please write your code here.
def primer(a,b):
    cnt=0
    for i in range(a,b+1):
        isprime=True
        for j in range(2,i):
            if i%j==0:
                isprime=False
        #print(isprime)
        if isprime:
            #print(i)
            if (i//10+ i%10)%2==0:
                cnt+=1

    return cnt

print(primer(a,b))