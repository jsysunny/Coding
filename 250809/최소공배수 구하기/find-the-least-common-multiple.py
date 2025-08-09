n, m = map(int, input().split())

# Please write your code here.
def maxa(n,m):
    for i in range(min(n,m),0,-1):
        if n%i==0 and m%i==0:
            return i
            break
    else:
        return "False"

i= maxa(n,m)
def mina(n,m,i):
    if i==False:
        print(n*m)
    else:
        print((n//i)*(m//i)*i)

mina(n,m,i)