a, b = map(int, input().split())

# Please write your code here.\
def multiply(a,b):
    if a==min(a,b):
        a=a*2
        b=b+25
    else:
        a=a+25
        b=b*2
    return a,b

a,b=multiply(a,b)
print(a,b)