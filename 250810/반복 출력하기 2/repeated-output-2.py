n = int(input())

# Please write your code here.
def Hello(n):
    if n==0:
        return
    Hello(n-1)
    print("HelloWorld")

Hello(n)