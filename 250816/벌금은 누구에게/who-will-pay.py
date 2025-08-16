N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

#print(student)
# Please write your code here.
stuset=[0]*N
ans=-1
for i in range(M):
    stuset[student[i]-1]+=1
    for i in range(N):
        if stuset[i]>=K:
            ans= i+1
            break

print(ans)
