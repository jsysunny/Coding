n = int(input())

# Please write your code here.
def right(n):
    if n==0:
        return
    right(n-1)
    print(n,end=" ")

def left(n):
    if n==0:
        return 
    print(n,end=" ")
    left(n-1)

right(n)
print()
left(n)