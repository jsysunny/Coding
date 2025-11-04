n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)
#print(a[0])
# Please write your code here.
max_score=0
for start_pos in range(1, 4):
    ball = start_pos
    score = 0
    for x, y, guess in moves:
        # 컵 위치 교환
        if ball == x:
            ball = y
        elif ball == y:
            ball = x
        # 추측 확인
        if ball == guess:
            score += 1
    max_score = max(max_score, score)

print(max_score)
    
    

