x1, x2, x3, x4 = map(int, input().split())

# Please write your code here.
def inter(x1,x2,x3,x4):
    if x1> x4 or x2< x3:
        return "nonintersecting"
    else:
        return "intersecting"

print(inter(x1,x2,x3,x4))