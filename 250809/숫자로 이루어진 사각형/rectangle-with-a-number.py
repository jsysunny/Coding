n = int(input())

# Please write your code here.
def rect(n):
    cnt=1
    for _ in range(n):
        for _ in range(n):
            print(cnt, end=" ")
            cnt+=1
            if cnt==10:
                cnt=1
        print()

rect(n)