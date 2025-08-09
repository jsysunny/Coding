n, m = map(int, input().split())

# Please write your code here.
def maxa(n,m):
    for i in range(min(n,m),0,-1):
        #print(i)
        if n%i==0 and m%i==0:
            print(i)
            break

maxa(n,m)