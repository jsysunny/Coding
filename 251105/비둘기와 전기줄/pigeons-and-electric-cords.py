N = int(input())
p=[list (map(int, input().split())) for i in range(N)]

#print(p)
pos = {}  # 줄 번호 -> 마지막으로 본 비둘기 위치
cnt = 0

for line, bird_pos in p:
    if line in pos:
        if pos[line] != bird_pos:
            cnt += 1
    pos[line] = bird_pos
print(cnt)