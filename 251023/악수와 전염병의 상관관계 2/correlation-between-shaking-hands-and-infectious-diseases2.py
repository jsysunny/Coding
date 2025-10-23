N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# 시간 순 정렬
handshakes.sort()

# 감염 여부
infected = [0] * (N + 1)
infected[P] = 1

# 감염자가 다른 사람을 감염시킬 수 있는 횟수
can_infect = [0] * (N + 1)
can_infect[P] = K

for t, x, y in handshakes:
    if infected[x] and can_infect[x] > 0 and not infected[y]:
        infected[y] = 1
        can_infect[x] -= 1
        can_infect[y] = K
    elif infected[y] and can_infect[y] > 0 and not infected[x]:
        infected[x] = 1
        can_infect[y] -= 1
        can_infect[x] = K

# 출력
for i in range(1, N + 1):
    print(infected[i], end="")