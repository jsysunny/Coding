N = int(input())

# Please write your code here.
cnt=0
def f(N):
    global cnt
    if N==1:
        return cnt
    cnt+=1
    if N%2==0:
        return f(N//2)
    else:
        return f(N//3)


print(f(N))
