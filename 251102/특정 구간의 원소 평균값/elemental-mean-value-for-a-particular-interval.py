n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.


cnt=0
for i in range(n):
    for j in range(i,n):
        suma=0
        for k in range(i,j+1):
            suma += arr[k]
        avg= suma/(j-i+1)
        for f in range(i,j+1):
            if suma % (j-i+1) ==0 and int(avg) == arr[f]:
                cnt+=1
                break
print(cnt)