N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

#print(student)
# Please write your code here.
penalties = [0] * (N + 1)  # 1번부터 N번 학생

ans = -1
for s in student:
    penalties[s] += 1
    if penalties[s] == K:
        ans = s
        break

print(ans)

