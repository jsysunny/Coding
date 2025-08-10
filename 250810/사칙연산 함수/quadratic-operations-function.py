a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def plus(a,c):
    return f"{a} + {c} = {a+c}"

def minus(a,c):
    return f"{a} - {c} = {a-c}"

def multiply(a,c):
    return f"{a} * {c} = {a*c}"

def split(a,c):
    return f"{a} / {c} = {int(a//c)}"


def calculate(a,o,c):
    if o=="+":
        return plus(a,c)
    elif o=="-":
        return minus(a,c)
    elif o=="*":
        return multiply(a,c)
    elif o=="/":
        return split(a,c)
    else:
        return False

print(calculate(a,o,c))