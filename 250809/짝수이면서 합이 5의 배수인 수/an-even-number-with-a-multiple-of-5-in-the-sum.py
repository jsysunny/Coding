n = int(input())

# Please write your code here.
def permit():
    return n%2==0 and (n//10+n%10)%5==0

if permit():
    print("Yes")
else:
    print("No")