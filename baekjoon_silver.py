#최대값 최소값 찾기
a=[38,21,53,62,19]
smallest=a[0]
for i in a:
    if i<smallest:
        smallest=i
#print(smallest)

# 선택 정렬 구현
for i in range(len(a)):
    # 가장 작은 값의 인덱스를 찾음
    min_index = i
    for j in range(i + 1, len(a)):
        if a[j] < a[min_index]:
            min_index = j
    # 현재 위치와 가장 작은 값을 교환
    a[i], a[min_index] = a[min_index], a[i]

#print(a)

# sort하기(오름차순)
a=['b','a','c']
a.sort() 
#print(a)

# 심화반 문제
#1
""" 아메리카노와 카페라테의 가격은 차가운 것과 뜨거운 것 상관없이 각각 4500, 5000원입니다. 
메뉴만 적은 것은 차가운 것으로 통일하고 아무거나를 적은 팀원의 것은 차가운 아메리카노로 통일하기로 했습니다.
각 직원이 적은 메뉴가 문자열 배열 order로 주어질때, 카페에서 결제하게 될 금액을 return 하는 solution함수를 작성해주세요
"""
#풀이

def solution(order_list):
    total_cost = 0
    for item in order_list:
        # 규칙 1: "anything" → 4,500원 (차가운 아메리카노)
        # 규칙 2: "americano"라는 단어가 들어있으면 → 4,500원
        # 규칙 3: 나머지(즉, "cafelatte" 등)는 5,000원
        if item == "anything" or "americano" in item:
            total_cost += 4500
        else:
            total_cost += 5000
    return total_cost

# 메인 실행부
if __name__ == "__main__":
    # 1) 주문 개수 N 입력
    N = int(input("주문개수를 입력하세요: ").strip())
    
    # 2) 주문 목록 입력 (N줄)
    order_list = []
    for _ in range(N):
        order_list.append(input().strip())
    
    # 3) 합계 계산
    answer = solution(order_list)
    
    # 4) 결과 출력
    print(answer)

#2
""" 실습용 로봇은 입력된 명령에 따라 x,y좌표로 표현되는 2차원 좌표 평면 위를 이동한다.
'R': 오른쪽으로 90도 회전, 'L': 왼쪽으로 90도 회전, 'G': 한 칸 전진, 'B': 한 칸 후진
처음에 (0,0) 위치에 +y축을 향하여 놓여있다. ex)"GRGLGRG"
"""
# 생각할게 지금 위치 + 방향 변화 direction 에 따를 위치 변화 dx[direction]= 새로운 위치 
# 풀이
def solution(command):
    direction = 0  # 0:북, 1:동, 2:남, 3:서
    x, y = 0, 0
    dx = [0, 1, 0, -1] # 방향별 위치 변화
    dy = [1, 0, -1, 0]

    for c in command:
        if c == 'R':
            direction = (direction + 1) % 4
        elif c == 'L':
            direction = (direction + 3) % 4
        elif c == 'G':
            x += dx[direction]
            y += dy[direction]
        elif c == 'B':
            x -= dx[direction]
            y -= dy[direction]

    return [x, y]

def solution(command):
    # 결과를 담을 리스트 (x, y)를 반환할 예정
    answer = []
    
    # 로봇의 방향(0=위, 1=오른쪽, 2=아래, 3=왼쪽)
    direction = 0
    # 초기 위치
    x, y = 0, 0
    
    for c in command:
        if c == 'R':
            # 오른쪽으로 90도
            direction = (direction + 1) % 4
        elif c == 'L':
            # 왼쪽으로 90도
            direction = (direction + 3) % 4  # (direction - 1) % 4 와 같음
        elif c == 'G':
            # 바라보는 방향으로 전진
            if direction == 0:    # 위쪽
                y += 1
            elif direction == 1:  # 오른쪽
                x += 1
            elif direction == 2:  # 아래쪽
                y -= 1
            else:                 # 왼쪽
                x -= 1
        elif c == 'B':
            # 바라보는 방향으로 후진
            if direction == 0:    # 위쪽
                y -= 1
            elif direction == 1:  # 오른쪽
                x -= 1
            elif direction == 2:  # 아래쪽
                y += 1
            else:                 # 왼쪽
                x += 1
        # 문제에서 'R', 'L', 'G', 'B' 외에는 없다고 가정
    
    # 최종 좌표를 answer에 담아서 반환
    answer.append(x)
    answer.append(y)
    
    return answer


# 메인 실행부: 사용자에게 명령어 문자열을 입력받고, 결과 출력
if __name__ == "__main__":
    cmd = input().strip()    # 예: "GRGLGRG"
    result = solution(cmd)   # [x, y] 형태의 리스트
    print(result)            # 예: [2, 2]

#3
"""
마라톤 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion
완주하지 못한 선수의 이름을 return하는 solution 함수를 작성해주세요
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion 길이는 participant 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있다.
참가자 중에는 동명이인이 있을 수 있다.
"""
# 풀이

def solution(participant, completion):
    answer = ''

    # (이름 -> 인원수) 딕셔너리
    dict_participant = {}
    
    # 1) 참가자 이름들을 각각 개수 세어 저장
    for p in participant:
        if p in dict_participant:
            dict_participant[p] += 1
        else:
            dict_participant[p] = 1
    
    # 2) 완주자 이름들을 순회하며 참가자 개수에서 차감
    for c in completion:
        if c in dict_participant:
            dict_participant[c] -= 1
    
    # 3) 남은 개수가 1 이상이면(= 아직 0이 안 되었으면) 완주 못한 사람
    for name, count in dict_participant.items():
        if count > 0:
            answer = name
            break
    
    return answer


# 메인 실행부
if __name__ == "__main__":

    # 1. 참가자 수 N
    N = int(input().strip())
    
    # 2. 참가자 명단 입력 (N명)
    participant = []
    for _ in range(N):
        participant.append(input().strip())
    
    # 3. 완주자 명단 입력 (N-1명)
    completion = []
    for _ in range(N - 1):
        completion.append(input().strip())
    
    # 4. 완주하지 못한 선수 찾기
    result = solution(participant, completion)
    
    # 5. 결과 출력
    print(result)


#4 
"""ROR 게임은 두 팀으로 나누어서 진행하며, 상대 팀 진영을 먼저 파괴하면 이기는 게임"""
# 풀이

def solution(maps):
    n = len(maps)      # 행(세로) 크기
    m = len(maps[0])   # 열(가로) 크기
    
    # 시작점이나 목표점이 벽(1)인 경우, 이동 불가
    if maps[0][0] == 0:
        return -1
    if maps[n-1][m-1] == 0:
        return -1
    
    # 방문 여부 표시
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    
    # 큐를 리스트로 사용 ( (x, y, 거리) 형태 )
    queue = [(0, 0, 1)]
    
    # 큐의 앞 인덱스 (pop(0) 대신 인덱스 이동)
    front_idx = 0
    
    # 상하좌우 이동
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    # BFS 진행
    while front_idx < len(queue):
        x, y, dist = queue[front_idx]
        front_idx += 1
        
        # 목표 지점 도달
        if x == n-1 and y == m-1:
            return dist
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            # 범위 내, 벽 아닌 곳(0), 미방문이면 이동
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist+1))
    
    # 끝까지 못 도달하면 -1
    return -1

# 메인 실행부: 사용자 입력
if __name__ == "__main__":
    
    # 맵 크기 입력
    n, m = map(int, input().split())
    
    # 맵 정보 입력
    maps = []
    for _ in range(n):
        row = list(map(int, input().split()))
        maps.append(row)
    
    # 해답 계산
    answer = solution(maps)
    print(answer)


#1. 주사위 문제
"""1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
#같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
#같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
#모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다."""

# 풀이

a, b, c = map(int, input("a, b, c 값을 입력하세요: ").split()) #공백으로 입력해야 함
# 2. 규칙에 따라 상금 계산
if a == b == c:
    # 같은 눈이 3개
    prize = 10000 + a * 1000
elif a == b or a == c:
    # 같은 눈이 2개 (a == b 또는 a == c)
    prize = 1000 + a * 100
elif b == c:
    # 같은 눈이 2개 (b == c)
    prize = 1000 + b * 100
else:
    # 모두 다른 눈
    prize = max(a, b, c) * 100
# 3. 결과 출력
print(prize)


# 2. 수빈이와 수열
""" 수빈이는 심심해서 수열을 가지고 놀고 있다. 먼저, 정수 수열 A를 쓴다. 
그리고 그 아래에 정수 수열 A의 해당 항까지의 평균값을 그 항으로 하는 정수 수열 B를 쓴다. 
예를 들어, 수열 A가 1, 3, 2, 6, 8이라면, 수열 B는 1/1, (1+3)/2, (1+3+2)/3, (1+3+2+6)/4, (1+3+2+6+8)/5, 즉, 1, 2, 2, 3, 4가 된다. 
수열 B가 주어질 때, 수빈이의 규칙에 따른 수열 A는 뭘까?
"""

# 풀이

N=int(input("길이를 입력하세요: "))
B=list(map(int,input("수열 B를 입력하세요: ").split()))

# S_prev = S_{i-1} (이전까지의 누적합), 초기값은 0
S_prev = 0
A = []

for i in range(1, N + 1):
    # 현재까지의 누적합 S_i = i * B[i-1]
    S_i = i * B[i - 1]
    # A_i = S_i - S_{i-1}
    A_i = S_i - S_prev
    A.append(A_i)
    # 다음 루프를 위해 S_prev 갱신
    S_prev = S_i
# 결과 출력

print("수열 A는:" ,A)
# 공백으로 구분하여 한 줄에 출력하는 것은 *A


# 3. 피보나치 수
"""
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
n=17일때 까지 피보나치 수를 써보면 다음과 같다.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
"""

# 풀이

n = int(input("몇번째인지 입력하세요:").strip())  # n 입력받기
# n=0이면 결과는 0, n=1이면 결과는 1이므로,
# 피보나치 수열을 저장하는 리스트를 처음 두 원소로 시작합니다.
fib = [0, 1]
# 2부터 n까지 순회하며 피보나치 수를 구합니다.
for i in range(2, n + 1):
    fib.append(fib[i-1] + fib[i-2])
# n번째 피보나치 수 출력
print(fib)
print(fib[n])


# 4. 행복
"""
코이 초등학교에 새로 부임하신 교장 선생님은 어린 학생들의 행복감과 학생들의 성적 차이 관계를 알아보기로 했다.
그래서 이전 성적을 조사하여 학생 들의 시험 점수 차이 변화를 알아보려고 한다.
예를 들어서 2016년 학생 8명의 점수가 다음과 같다고 하자.
27, 35, 92, 75, 42, 53, 29, 87
그러면 가장 높은 점수는 92점이고 가장 낮은 점수는 27점이므로 점수의 최대 차이는 65이다. 한편 2017년 학생 8명의 점수가 다음과 같았다.
85, 42, 79, 95, 37, 11, 72, 32
이때 가장 높은 점수는 95점이고 가장 낮은 점수는 11점이므로 점수의 최대 차이는 84이다.
N명 학생들의 점수가 주어졌을 때, 가장 높은 점수와 가장 낮은 점수의 차이를 구하는 프로그램을 작성하시오
"""
# 풀이 

# N : 학생 수
N = int(input("학생 수를 입력하세요: ").strip())
# N명의 학생 점수를 리스트로 입력받습니다.
scores = list(map(int, input("점수를 list로 입력하세요: ").split()))
# 가장 높은 점수 - 가장 낮은 점수
difference = max(scores) - min(scores)
print(difference)

N = int(input().strip())
scores = list(map(int, input().split()))
# 초기값을 첫 번째 요소로 설정
maximum = scores[0]
minimum = scores[0]
# 나머지 요소들을 순회하며 최대/최소 비교 갱신
for score in scores[1:]:
    if score > maximum:
        maximum = score
    if score < minimum:
        minimum = score
print(maximum - minimum)


# 6.보너스점수
"""
OX표에 N개의 문제들이 있을 때, 1번 문제, 2번 문제, ..., N번 문제 순으로 채점된다.
문제는 뒤로 갈수록 어려워지기 때문에, i 번 문제의 기본 점수는 i 점이다.
문제를 맞히면 그 문제의 기본 점수(즉 i 번 문제의 경우 i 점)를 획득하며, 틀리면 얻지 못한다.
기본 점수와 별개로, '보너스 점수'라는 값이 존재한다. 이는 처음에는 0점이다.
문제를 맞히면 그 때의 '보너스 점수'를 획득하고, '보너스 점수'의 값이 1점 증가한다.
문제를 틀리면 '보너스 점수'를 얻지 못하고, '보너스 점수'의 값이 0점으로 초기화된다.
"""
# 풀이

N = int(input("문제수를 입력하세요:" ).strip())
S = list(map(input("배열을 입력하세요:").strip()))
total_score = 0
bonus_score = 0  # '보너스 점수'는 처음에 0
# i번째 문제(인덱스는 0부터 시작)에 대해,
# 맞히면 base_score(i+1) + bonus_score를 얻고 bonus_score가 1 증가
# 틀리면 bonus_score는 0으로 초기화
for i in range(N):
    if S[i] == 'O':
        # 기본 점수: (i+1)
        # 보너스 점수: bonus_score
        total_score += (i + 1) + bonus_score
        bonus_score += 1
    else:
        bonus_score = 0
print(total_score)


# 6. 블랙잭
"""
카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 있다.
한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.
김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.
이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.
"""
# 풀이 

N, M = map(int, input("N과 M을 입력하세요: ").split())
cards = list(map(int, input("카드를 배열로 입력하세요: ").split()))
answer = 0  # 최적의 합(초기값 0)
# 모든 3장의 조합을 탐색 (3중 for 문)
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            card_sum = cards[i] + cards[j] + cards[k]
            # M을 넘지 않으면서, 현재까지의 최대값보다 크면 갱신
            if card_sum <= M and card_sum > answer:
                answer = card_sum
print(answer)

# 7.일곱난쟁이
"""
왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.
아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.
아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.
입력
아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.
출력
일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.
"""
# 풀이

# 1. 아홉 난쟁이의 키를 입력받아 리스트에 저장
dwarfs = list(map(int(input("아홉난쟁이의 키를 입력하세요:").strip())))
# 2. 아홉 난쟁이 키의 총합
total = sum(dwarfs)
# 3. 두 난쟁이를 골라서 그 난쟁이들 키를 제외했을 때 합이 100이 되는지 검사
found = False
for i in range(9):
    for j in range(i + 1, 9):
        if total - (dwarfs[i] + dwarfs[j]) == 100:
            # 찾았다면, 이 두 명을 제외한 나머지가 "참 난쟁이 7명"이 됨
            fake1 = dwarfs[i]
            fake2 = dwarfs[j]
            found = True
            break
    if found: # 외부 루프 나오기
        break
# 4. 두 난쟁이를 제외하고 오름차순으로 출력
real_dwarfs = [h for h in dwarfs if h not in (fake1, fake2)]
real_dwarfs.sort()
for h in real_dwarfs:
    print(h)


#8. 트럭주차
"""상근이는 트럭을 총 세 대 가지고 있다. 오늘은 트럭을 주차하는데 비용이 얼마나 필요한지 알아보려고 한다.
상근이가 이용하는 주차장은 주차하는 트럭의 수에 따라서 주차 요금을 할인해 준다.
트럭을 한 대 주차할 때는 1분에 한 대당 A원을 내야 한다. 두 대를 주차할 때는 1분에 한 대당 B원, 세 대를 주차할 때는 1분에 한 대당 C원을 내야 한다.
A, B, C가 주어지고, 상근이의 트럭이 주차장에 주차된 시간이 주어졌을 때, 주차 요금으로 얼마를 내야 하는지 구하는 프로그램을 작성하시오.
입력
첫째 줄에 문제에서 설명한 주차 요금 A, B, C가 주어진다. (1 ≤ C ≤ B ≤ A ≤ 100)
다음 세 개 줄에는 두 정수가 주어진다. 이 정수는 상근이가 가지고 있는 트럭이 주차장에 도착한 시간과 주차장에서 떠난 시간이다. 도착한 시간은 항상 떠난 시간보다 앞선다. 입력으로 주어지는 시간은 1과 100사이 이다.
출력
첫째 줄에 상근이가 내야하는 주차 요금을 출력한다.
"""
# 풀이

# 1. 주차 요금 A, B, C 입력받기
A, B, C = map(int, input("A,B,C를 입력하세요: ").split())
# 2. 트럭 3대의 도착/떠난 시간을 저장
times = []

for i in range(3): 
    start, end = map(int, input(f"트럭 {i+1} 의 도착/떠난 시간을 입력하세요: ").split()) #f"{chr(65 + i)} 
    times.append((start,end))

# 3. 시간대별로 주차 중인 트럭 수를 셀 리스트(인덱스 0~100 사용)
timeline = [0] * 101
# 4. 각 트럭의 [도착 시간, 떠난 시간) 구간에 대해
#    해당 시간대(t)마다 주차 트럭 수를 +1
for start, end in times:
    for t in range(start, end):
        timeline[t] += 1
# 5. 최종 요금 계산
total_cost = 0
for t in range(1, 101):
    if timeline[t] == 1:
        total_cost += A * 1
    elif timeline[t] == 2:
        total_cost += B * 2
    elif timeline[t] == 3:
        total_cost += C * 3
# 6. 출력
print(total_cost)


#9. 이름궁합 테스트
"""
시윤이는 좋아하는 이성이 생기면 가장 먼저 이름궁합부터 본다. 이름궁합을 보는 방법은 간단하다. 먼저 이름을 알파벳 대문자로 적는다. 각 알파벳 대문자에는 다음과 같이 알파벳을 적는데 필요한 획수가 주어진다. 예를 들어, 두 사람의 이름인 LEESIYUN, MIYAWAKISAKURA 를 같이 표현했을 때 다음과 같이 먼저 주어진 이름부터 한 글자씩 적는다.

알파벳	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
획수	3	2	1	2	4	3	1	3	1	1	3	1	3	2	1	2	2	2	1	2	1	1	1	2	2	1
두 사람의 이름을 알파벳 대문자로 표현한 뒤, 한 글자씩 번갈아가며 적는다.

예시 :  L M E I E Y S A I W Y A U K N I S A K U R A

예시처럼 이름이 남을 경우엔 뒤에 남은 글자인 S A K U R A를 맨 뒤에 적는다. 그러고 나서 알파벳을 대응하는 숫자로 바꾸고 각 숫자와 그 숫자의 오른쪽 숫자와 더한 것을 밑에 적는다. 더한 숫자가 10이 넘을 경우엔 일의 자리 수만 남긴다. 이 과정을 반복하여 숫자가 2개만 남았을 때 남은 숫자가 두 사람의 궁합이 좋을 확률이 된다.

과정을 자세히 나타내면 다음과 같다.

초기 상태 : 1 3 4 1 4 2 1 3 1 1 2 3 1 3 2 1 1 3 3 1 2 3
한번 수행 :  4 7 5 5 6 3 4 4 2 3 5 4 4 5 3 2 4 6 4 3 5
두번 수행 :   1 2 0 1 9 7 8 6 5 8 9 8 9 8 5 6 0 0 7 8
세번 수행 :    3 2 1 0 6 5 4 1 3 7 7 7 7 3 1 6 0 7 5
...
19번 수행 :                  5 7 0
20번 수행 :                   2 7
따라서 LEESIYUN와 MIYAWAKISAKURA이 궁합이 좋을 확률이 27%이다
"""
#풀이

def solution(A, B):
    # 알파벳 대문자 -> 획수 매핑
    strokes = {
        'A':3,'B':2,'C':1,'D':2,'E':4,'F':3,'G':1,'H':3,'I':1,'J':1,
        'K':3,'L':1,'M':3,'N':2,'O':1,'P':2,'Q':2,'R':2,'S':1,'T':2,
        'U':1,'V':1,'W':1,'X':2,'Y':2,'Z':1
    }
    
    lenA = len(A)
    lenB = len(B)
    
    # 1) 두 이름 번갈아 합치기
    merged = []
    i = 0
    while i < lenA or i < lenB:
        if i < lenA:
            merged.append(A[i])
        if i < lenB:
            merged.append(B[i])
        i += 1
    # merged: 번갈아가며 합쳐진 문자 리스트
    
    # 2) 각 문자 -> 획수 숫자로 변환
    nums = [strokes[ch] for ch in merged]
    
    # 3) 인접 숫자 합산 -> 일의 자리만 (길이가 2가 될 때까지 반복)
    while len(nums) > 2:
        new_nums = []
        for i in range(len(nums) - 1):
            s = (nums[i] + nums[i+1]) % 10
            new_nums.append(s)
        nums = new_nums
    
    # 4) 마지막 2개를 붙여서 결과 (00~99)
    result_2digit = nums[0] * 10 + nums[1]  # 십의자리 * 10 + 일의자리
    
    # 5) 십의 자리가 0이면 생략, 그렇지 않으면 그대로
    if result_2digit < 10:
        return f"{result_2digit}%"
    else:
        return f"{result_2digit}%"


# 메인 실행부
if __name__ == "__main__":

    # 1) N, M 입력
    N, M = map(int, input().split())
    # 2) A와 B 입력
    A, B = input().split()
    
    # 3) 해결
    answer = solution(A, B)
    # 4) 출력
    print(answer)



#10. 자리에 누울 곳 찾기
"""
일 년 동안 세계일주를 하던 영식이는 여행을 하다 너무 피곤해서 근처에 있는 코레스코 콘도에서 하룻밤 잠을 자기로 하고 방을 잡았다.

코레스코 콘도에 있는 방은 NxN의 정사각형모양으로 생겼다. 방 안에는 옮길 수 없는 짐들이 이것저것 많이 있어서 영식이의 누울 자리를 차지하고 있었다. 영식이는 이 열악한 환경에서 누울 수 있는 자리를 찾아야 한다. 영식이가 누울 수 있는 자리에는 조건이 있다. 똑바로 연속해서 2칸 이상의 빈 칸이 존재하면 그 곳에 몸을 양 옆으로 쭉 뻗으면서 누울 수 있다. 가로로 누울 수도 있고 세로로 누울 수도 있다. 누울 때는 무조건 몸을 쭉 뻗기 때문에 반드시 벽이나 짐에 닿게 된다. (중간에 어정쩡하게 눕는 경우가 없다.)

만약 방의 구조가 위의 그림처럼 생겼다면, 가로로 누울 수 있는 자리는 5개이고, 세로로 누울 수 있는 자리는 4개 이다. 방의 크기 N과 방의 구조가 주어졌을 때, 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 방의 크기 N이 주어진다. N은 1이상 100이하의 정수이다. 그 다음 N줄에 걸쳐 N개의 문자가 들어오는데 '.'은 아무것도 없는 곳을 의미하고, 'X'는 짐이 있는 곳을 의미한다.

출력
첫째 줄에 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 개수를 출력한다.

예제 입력 1 
5
....X
..XX.
.....
.XX..
X....
예제 출력 1 
5 4
"""
# 풀이

def solve(N, room):
    # 가로로 누울 수 있는 자리 (이중 리스트 행 기준)
    horizontal_count = 0
    for row in room:
        continuous = 0  # 연속된 '.' 개수
        for char in row:
            if char == '.':
                continuous += 1
            else:  # 'X'를 만나면 확인 후 초기화
                if continuous >= 2:
                    horizontal_count += 1
                continuous = 0
        # 행 끝이 '.'으로 끝난 경우도 확인
        if continuous >= 2:
            horizontal_count += 1

    # 세로로 누울 수 있는 자리 (이중 리스트 열 기준)
    vertical_count = 0
    for col in range(N):
        continuous = 0
        for row_idx in range(N):
            if room[row_idx][col] == '.':
                continuous += 1
            else:
                if continuous >= 2:
                    vertical_count += 1
                continuous = 0
        if continuous >= 2:
            vertical_count += 1

    # 두 개의 값을 한꺼번에 반환
    return horizontal_count, vertical_count


if __name__ == "__main__":
    N = int(input().strip())
    room = [input().rstrip() for _ in range(N)]

    # 함수에서 결과를 받음
    h_count, v_count = solve(N, room)

    # 반환된 값 출력
    print(h_count, v_count)


#11.더하기 사이클
"""
0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 
그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.
26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.
출력
첫째 줄에 N의 사이클 길이를 출력한다.
"""
#풀이

def cycle_length(N):
    # 사이클 계산
    original = N  # 처음 주어진 수
    count = 0     # 사이클 길이(반복 횟수)

    current = N
    while True:
        count += 1
        # 1) 각 자리 합을 구한다
        #   - 10보다 작으면 앞에 0을 붙여야 한다고 했지만,
        #     실제로는 자리수를 분리할 때 0이 자동으로 처리됨
        tens = current // 10         # 10의 자리
        ones = current % 10          # 1의 자리
        sum_digit = (tens + ones) % 10  # 각 자리수 합의 1의 자리

        # 2) 새로운 수 = (오른쪽 자리: current의 1의 자리) * 10 + (앞에서 구한 합의 1의 자리)
        new_num = ones * 10 + sum_digit

        current = new_num
        
        # 처음 수와 같다면 중단
        if current == original:
            break

    return count


if __name__ == "__main__":

    N = int(input().strip())
    print(cycle_length(N))


#12. 디지털 티비
"""
상근이는 채널 리스트를 조절해 KBS1을 첫 번째로, KBS2를 두 번째로 만들려고 한다.
티비를 켜면 디지털 수신기는 시청 가능한 채널 리스트를 보여준다. 
모든 채널의 이름은 서로 다르고, 항상 KBS1과 KBS2를 포함하고 있다. 
상근이는 이 리모콘을 이용해서 리스트의 순서를 바꾸는 법을 알아냈다. 
리스트의 왼편에는 작은 화살표가 있고, 이 화살표는 현재 선택한 채널을 나타낸다. 가장 처음에 화살표는 제일 첫 번째 채널을 가리키고 있다.
다음과 같은 네 가지 버튼을 이용해서 리스트의 순서를 바꿀 수 있다. 각각은 1번부터 4번까지 번호가 적혀져있는 버튼이다.

1.화살표를 한 칸 아래로 내린다. (채널 i에서 i+1로)
2.화살표를 위로 한 칸 올린다. (채널 i에서 i-1로)
3.현재 선택한 채널을 한 칸 아래로 내린다. (채널 i와 i+1의 위치를 바꾼다. 화살표는 i+1을 가리키고 있는다)
4.현재 선택한 채널을 위로 한 칸 올린다. (채널 i와 i-1의 위치를 바꾼다. 화살표는 i-1을 가리키고 있다)
화살표가 채널 리스트의 범위를 넘어간다면, 그 명령은 무시한다.
현재 채널 리스트의 순서가 주어졌을 때, KBS1를 첫 번째로, KBS2를 두 번째로 순서를 바꾸는 방법을 구하는 프로그램을 작성하시오.
방법의 길이는 500보다 작아야 한다."""

#풀이

def solve(N,channels):

    # 버튼 누른 기록(문자들)을 저장할 리스트
    commands = []

    # 처음 포인터는 0번 채널 가리킴
    pointer = 0

    # 도우미 함수: 버튼 1 (포인터 아래 이동)
    def press_1():
        nonlocal pointer
        if pointer < N - 1:   # 아직 맨 아래가 아니면
            pointer += 1
            commands.append('1')

    # 도우미 함수: 버튼 2 (포인터 위 이동)
    def press_2():
        nonlocal pointer
        if pointer > 0:      # 아직 맨 위가 아니면
            pointer -= 1
            commands.append('2')

    # 도우미 함수: 버튼 3 (swap 아래, pointer++)
    def press_3():
        nonlocal pointer
        if pointer < N - 1:  # 아래 칸이 존재해야 swap 가능
            channels[pointer], channels[pointer+1] = channels[pointer+1], channels[pointer]
            pointer += 1
            commands.append('3')

    # 도우미 함수: 버튼 4 (swap 위, pointer--)
    def press_4():
        nonlocal pointer
        if pointer > 0:      # 위 칸이 존재해야 swap 가능
            channels[pointer], channels[pointer-1] = channels[pointer-1], channels[pointer]
            pointer -= 1
            commands.append('4')

    # ----------------------------------------------------------------
    # 1) KBS1을 맨 위(인덱스 0)로 올리기
    # ----------------------------------------------------------------
    # 1-1) KBS1의 현재 인덱스를 찾는다.
    idx1 = channels.index("KBS1")
    
    # 1-2) 포인터를 KBS1이 있는 위치(idx1)까지 '버튼 1'로 이동
    #      (pointer < idx1 인 동안 아래로 이동)
    while pointer < idx1:
        press_1()  # pointer++

    # 1-3) 이제 KBS1을 인덱스0으로 만들기 위해,
    #      (idx1번만큼) '버튼 4' 를 누르면 채널이 한 칸씩 위로 올라감
    while idx1 > 0:
        press_4()  # pointer--, 채널 스왑
        idx1 -= 1  # KBS1 위치가 한 칸 올라갔으므로

    # ----------------------------------------------------------------
    # 2) KBS2를 인덱스 1로 만들기
    # ----------------------------------------------------------------
    idx2 = channels.index("KBS2")  # KBS2의 현재 인덱스 (KBS1 이동 후 바뀌었을 수 있음)

    # 2-1) 포인터가 idx2가 되도록 아래로 이동 (버튼 1)
    while pointer < idx2:
        press_1()

    # 2-2) KBS2를 인덱스1로 만들기 위해, idx2 > 1 동안 '버튼 4'
    while idx2 > 1:
        press_4()
        idx2 -= 1

    # ----------------------------------------------------------------
    # 결과 출력: 누른 버튼을 이어붙인 문자열
    # ----------------------------------------------------------------
    return commands


if __name__ == "__main__":
    
    N = int(input().strip())
    channels = [input().strip() for _ in range(N)]

    result= solve(N,channels)
    print(result)


# 13. 기러기
"""
알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.
팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다. 
level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.
"""
#풀이

word = input().strip()  # 알파벳 소문자로 이루어진 단어 입력

# 팰린드롬 판별: 문자열과 거꾸로 뒤집은 문자열이 같은지 확인
if word == word[::-1]:
    print("팰린드롬입니다!")
else:
    print("팰린드롬이 아닙니다.")


#14. 암호화
""" 알파벳 을 각각 13개씩 미루고 알파벳이 아닌 경우 그대로 """
# 풀이

def rot13(text):
    result = []
    for char in text:
        # 대문자 범위 검사
        if 'A' <= char <= 'Z':
            # (아스키 코드로 변환, 13 더하고, Z를 넘어가면 A부터 이어붙이기)
            # ord('A')=65
            shifted = (ord(char) - ord('A') + 13) % 26 + ord('A')
            result.append(chr(shifted))
        # 소문자 범위 검사
        elif 'a' <= char <= 'z':
            shifted = (ord(char) - ord('a') + 13) % 26 + ord('a')
            result.append(chr(shifted))
        else:
            # 알파벳이 아닌 경우(공백, 숫자, 기호 등)는 그대로
            result.append(char)
    
    return "".join(result)


if __name__ == "__main__":
    text = str(input().strip())  
    print(rot13(text))



# 15. 사과 담기 게임
"""
상근이는 오락실에서 바구니를 옮기는 오래된 게임을 한다. 스크린은 N칸으로 나누어져 있다. 스크린의 아래쪽에는 M칸을 차지하는 바구니가 있다. 
(M<N) 플레이어는 게임을 하는 중에 바구니를 왼쪽이나 오른쪽으로 이동할 수 있다. 
하지만, 바구니는 스크린의 경계를 넘어가면 안 된다. 가장 처음에 바구니는 왼쪽 M칸을 차지하고 있다.
스크린의 위에서 사과 여러 개가 떨어진다. 각 사과는 N칸중 한 칸의 상단에서 떨어지기 시작하며, 스크린의 바닥에 닿을때까지 직선으로 떨어진다. 
한 사과가 바닥에 닿는 즉시, 다른 사과가 떨어지기 시작한다.
바구니가 사과가 떨어지는 칸을 차지하고 있다면, 바구니는 그 사과가 바닥에 닿을 때, 사과를 담을 수 있다. 
상근이는 사과를 모두 담으려고 한다. 이때, 바구니의 이동 거리의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M < N ≤ 10) 둘째 줄에 떨어지는 사과의 개수 J가 주어진다. (1 ≤ J ≤ 20) 다음 J개 줄에는 사과가 떨어지는 위치가 순서대로 주어진다.
출력
모든 사과를 담기 위해서 바구니가 이동해야 하는 거리의 최솟값을 출력한다.

예제 입력 1 
5 1
3
1
5
3
예제 출력 1 
6
"""

# 풀이

def minimum_basket_movement(N, M, J, apple_positions):
    # 초기 바구니 위치 (왼쪽 끝 기준으로 시작)
    basket_left = 1
    basket_right = M
    total_movement = 0

    for apple in apple_positions:
        if basket_left <= apple <= basket_right:
            # 사과가 바구니 범위 안에 떨어지면 이동할 필요 없음
            continue
        elif apple < basket_left:
            # 사과가 바구니 왼쪽에 떨어질 경우
            move_distance = basket_left - apple
            basket_left -= move_distance
            basket_right -= move_distance
            total_movement += move_distance
        elif apple > basket_right:
            # 사과가 바구니 오른쪽에 떨어질 경우
            move_distance = apple - basket_right
            basket_left += move_distance
            basket_right += move_distance
            total_movement += move_distance

    return total_movement

# 입력 
N, M = map(int,input().split())
J = int(input().strip())
apple_positions = list(int,input().strip())

# 함수 실행 및 결과 출력
result = minimum_basket_movement(N, M, J, apple_positions)
print(result)


# 이름 정렬하기
"""
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)
둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 
나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 
길이가 100보다 작거나 같은 문자열이다. 입력은 가입한 순서로 주어진다.
출력
첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.

예제 입력 1 
3
21 Junkyu
21 Dohyun
20 Sunyoung
예제 출력 1 
20 Sunyoung
21 Junkyu
21 Dohyun
"""
# 풀이

def sort_members_by_age(N, members):
    # 나이와 가입 순서를 기준으로 정렬 (풀어서 구현)
    for i in range(len(members)):
        for j in range(len(members) - i - 1):
            # 첫 번째 기준: 나이 비교
            if members[j][0] > members[j + 1][0]:
                members[j], members[j + 1] = members[j + 1], members[j]
            # 두 번째 기준: 나이가 같으면 가입 순서 비교
            elif members[j][0] == members[j + 1][0] and members[j][2] > members[j + 1][2]:
                members[j], members[j + 1] = members[j + 1], members[j]
    return [(age, name) for age, name, _ in members]


# 메인 함수 호출
if __name__ == "__main__":
    N = int(input("회원 수를 입력하세요: "))
    members = []
    for i in range(N):
        age, name = input("나이와 이름을 입력하세요: ").split()
        members.append((int(age), name, i))  # i=가입 순서, 파이썬은 문자열로 받기때문에 int로 형변환 해줘야 함

    sorted_members = sort_members_by_age(N, members)

    for age, name in sorted_members:
        print(age, name)



# 좌표 정렬하기
"""
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. 
(-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

예제 입력 1 
5
3 4
1 1
1 -1
2 2
3 3
예제 출력 1 
1 -1
1 1
2 2
3 3
3 4
"""
# 풀이

def sort_points(points):
    # x좌표를 기준으로 정렬, x좌표가 같으면 y좌표로 정렬
    for i in range(len(points)):
        for j in range(len(points) - i - 1):
            if points[j][0] > points[j + 1][0] or (points[j][0] == points[j + 1][0] and points[j][1] > points[j + 1][1]):
                points[j], points[j + 1] = points[j + 1], points[j]
    return points

# 메인 함수 호출
N = int(input("점의 개수를 입력하세요: "))
points = []
for _ in range(N):
    x, y = map(int, input("점의 좌표를 입력하세요: ").split())
    points.append((x, y))

sorted_points = sort_points(points)

for x, y in sorted_points:
    print(x, y)
"""
# 수 정렬 (중복제거, 오름차순 )
"""
def sort_numbers(n, numbers):
    # 중복 제거
    unique_numbers = list(set(numbers))

    # 정렬 구현 (버블 정렬로 구현)
    for i in range(len(unique_numbers)):
        for j in range(len(unique_numbers) - i - 1):
            if unique_numbers[j] > unique_numbers[j + 1]:
                unique_numbers[j], unique_numbers[j + 1] = unique_numbers[j + 1], unique_numbers[j]

    return unique_numbers

# 메인 함수 호출
N = int(input("수의 개수를 입력하세요: "))
numbers = []
for _ in range(N):
    num = int(input("수를 입력하세요: "))
    numbers.append(num)

sorted_numbers = sort_numbers(N, numbers)

for number in sorted_numbers:
    print(number)



# candy war
"""
알고리즘 유치원 선생님인 영희는 간식시간이 되자 아이들에게 사탕을 나누어 주려고 하였다. 
일단 모든 아이들이 원으로 둘러 앉는다. 그리고 모든 아이들은 동시에 자기가 가지고 있는 사탕의 절반을 오른쪽 아이에게 준다. 
만약 이 결과 홀수개의 사탕을 가지게 된 아이가 있을 경우 선생님이 한 개를 보충해 짝수로 만들어 주기로 했다. 
흥미로워 보이는 이 놀이에 아이들은 참여 했고 이 과정을 몇 번 거치자 자연스럽게 모든 아이들이 같은 수의 사탕을 가지게 되어 소란은 종료되었다.
자기가 가진 사탕의 반을 옆에 오른쪽에 앉은 아이에게 주는 과정과 선생님이 사탕을 보충해 주는 과정을 묶어서 1 순환이라고 할 때 몇 번의 순환을 거치면 
모든 아이들이 같은 수의 사탕을 가지게 되는지 계산 해보자. 
단, 처음부터 홀수개의 사탕을 가지고 있으면 선생님이 짝수로 보충을 먼저 해주며 이 경우 순환수에 들어가지 않는다. 
선생님은 충분한 수의 사탕을 갖고 있다고 가정하자.
입력
입력은 표준입력(standard input)을 통해 받아들인다. 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
각각의 테스트 케이스의 첫 줄에는 아이의 인원 N (1 ≤ N ≤ 10)이 주어지고
 그 다음 줄에는 각 아이들이 초기에 가지고 있는 사탕의 개수 Ci ( 1 ≤ i ≤ N, 1 ≤ Ci ≤ 30)가 주어진다. 
 분배 시 C1의 오른쪽에는 C2가, C2의 오른쪽에는 C3가…… 같은 식으로 앉게 되며 CN의 오른쪽에는 C1이 앉게 된다.
출력
출력은 표준출력(standard output)을 통하여 출력한다. 각 테스트 케이스에 대하여 모든 아이가 같은 개수의 사탕을 가질 때까지 몇 순환이 걸리는지 출력하시오.
"""
# 풀이

def distribute_candies(candies):
    n = len(candies)
    cycles = 0

    # Ensure all candies are even initially
    candies = [c + (c % 2) for c in candies]

    while len(set(candies)) != 1:
        # Distribute candies
        half_candies = [c // 2 for c in candies]
        for i in range(n):
            candies[i] = half_candies[i] + half_candies[i - 1]

        # Make candies even again
        candies = [c + (c % 2) for c in candies]

        cycles += 1

    return cycles

# Main logic to read input and process test cases
import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])  # Number of test cases
results = []

for t in range(T):
    N = int(data[t * 2 + 1])  # Number of children
    candies = list(map(int, data[t * 2 + 2].split()))
    results.append(distribute_candies(candies))

for result in results:
    print(result)


# 판화
"""
문제
W대학교 미술대학 조소과에서는 지루한 목판화 작업을 하는 학생들을 돕기 위해 판화 기계를 제작하였다.
기계는 로봇 팔이 쥔 조각도를 상하좌우 네 방향으로 움직일 수 있는 구조로서, 조각도 아래에 목판을 놓으면 그 위에 선들을 자동으로 그어주는 기능을 가지고 있다.
목판에는 N2개의 점들이 일정한 간격으로 N행 N열의 격자모양을 이루며 찍혀있다. 처음 로봇의 조각도를 올려놓는 위치는 항상 이 점들 중 맨 왼쪽 맨 위의 꼭짓점이다.
로봇 팔을 움직이는 명령의 순서가 주어졌을 때, 목판 위에 패인 조각도의 혼적을 출력하는 프로그램을 작성하시오.
판화 기계는 작동 도중 로봇 팔이 격자 바깥으로 나가도록 하는 움직임 명령을 만나면, 무시하고 그 다음 명령을 진행한다.

입력
첫째 줄에 목판의 크기 N (2 ≤ N ≤ 10)이 주어진다. 행 열의 점들이 찍혀 있다는 의미이다. 둘째 줄에 로봇팔의 움직임이 한 줄로 공백 없이 입력된다. 
위쪽으로 이동은 'U', 아래쪽으로 이동은 'D', 왼쪽으로 이동은 'L', 오른쪽으로 이동은 'R'로 표시된다. 
로봇팔의 움직임을 나타내는 이 문자열의 길이는 최대 250이다.
출력
로봇팔이 지나지 않은 점은 '.'으로, 로봇팔이 수직 방향으로만 지난 점은 '|'으로, 로봇팔이 수평 방향으로만 지난 점은 '-'으로, 수직과 수평 방향 모두로 지난 점은 '+'로 표기하도록 한다.
 네 문자의 ASCII 코드는 각각 46, 124, 45, 43이다.

예제 입력 1 
5
DRDRRUU
예제 출력 1 
|..|.
++.|.
.+-+.
.....
.....
"""
# 풀이

def execute_robot_commands(n, commands):
    # Initialize the board with '.'
    board = ['.' *n for _ in range(n)]

    # Starting position
    x, y = 0, 0
    board[x][y] = '.'  # Initially the robot starts here

    # Movement deltas for U, D, L, R
    movements = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    # Process each command
    for command in commands:
        dx, dy = movements[command]
        nx, ny = x + dx, y + dy

        # Check boundaries
        if 0 <= nx < n and 0 <= ny < n:
            # Update the current and new position
            if command in ('U', 'D'):
                board[x][y] = '|' if board[x][y] in ('.', '|') else '+'
            elif command in ('L', 'R'):
                board[x][y] = '-' if board[x][y] in ('.', '-') else '+'

            x, y = nx, ny  # Move to the new position

            # Update the new position after moving
            if command in ('U', 'D'):
                board[x][y] = '|' if board[x][y] in ('.', '|') else '+'
            elif command in ('L', 'R'):
                board[x][y] = '-' if board[x][y] in ('.', '-') else '+'

    return board

# Main logic
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])  # Size of the board
    commands = data[1]  # Movement commands

    result_board = execute_robot_commands(n, commands)

    for row in result_board:
        print(''.join(row))


# 참외 면적 구하기
"""
1m2의 넓이에 자라는 참외의 개수는 헤아렸고, 이제 참외밭의 넓이만 구하면 된다. 
참외밭은 ㄱ-자 모양이거나 ㄱ-자를 90도, 180도, 270도 회전한 모양(┏, ┗, ┛ 모양)의 육각형이다.
다행히도 밭의 경계(육각형의 변)는 모두 동서 방향이거나 남북 방향이었다. 밭의 한 모퉁이에서 출발하여 밭의 둘레를 돌면서 밭경계 길이를 모두 측정하였다.
그림에서 오른쪽은 동쪽, 왼쪽은 서쪽, 아래쪽은 남쪽, 위쪽은 북쪽이다.
이 그림의 왼쪽위 꼭짓점에서 출발하여, 
반시계방향으로 남쪽으로 30m, 동쪽으로 60m, 남쪽으로 20m, 동쪽으로 100m, 북쪽으로 50m, 서쪽으로 160m 이동하면 다시 출발점으로 되돌아가게 된다.
위 그림의 참외밭  면적은 6800m2이다. 만약 1m2의 넓이에 자라는 참외의 개수가 7이라면, 이 밭에서 자라는 참외의 개수는 47600으로 계산된다.
1m2의 넓이에 자라는 참외의 개수와, 참외밭을 이루는 육각형의 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돌면서 
지나는 변의 방향과 길이가 순서대로 주어진다. 이 참외밭에서 자라는 참외의 수를 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 1m2의 넓이에 자라는 참외의 개수를 나타내는 양의 정수 K (1 ≤ K ≤ 20)가 주어진다. 
참외밭을 나타내는 육각형의 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돌면서 지나는 변의 방향과 길이 (1 이상 500 이하의 정수) 가
둘째 줄부터 일곱 번째 줄까지 한 줄에 하나씩 순서대로 주어진다. 변의 방향에서 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4로 나타낸다.

출력
첫째 줄에 입력으로 주어진 밭에서 자라는 참외의 수를 출력한다.

예제 입력 1 
7
4 50
2 160
3 30
1 60
3 20
1 100
예제 출력 1 
47600
"""
# 풀이

# Store the lengths and their directions
def calculate_melons(k, directions_lengths):
    lengths = [length for _, length in directions_lengths]

    # Find the maximum width and height to determine the outer rectangle area
    max_width = max(length for direction, length in directions_lengths if direction in [1, 2])
    max_height = max(length for direction, length in directions_lengths if direction in [3, 4])

    # Find the indices of max width and height
    max_width_index = lengths.index(max_width)
    max_height_index = lengths.index(max_height)

    # Find the smaller rectangle dimensions
    small_width = abs(lengths[(max_width_index - 1) % 6] - lengths[(max_width_index + 1) % 6])
    small_height = abs(lengths[(max_height_index - 1) % 6] - lengths[(max_height_index + 1) % 6])

    # Calculate the areas
    big_area = max_width * max_height
    small_area = small_width * small_height

    # Calculate the actual field area and number of melons
    field_area = big_area - small_area
    total_melons = field_area * k

    return total_melons

# Main logic
if __name__ == "__main__":
    k = int(input())

# 두 번째 줄부터 입력 (directions_lengths)
    directions_lengths = []
    for _ in range(6):
        direction, length = map(int, input().split())
        directions_lengths.append((direction, length))

    result = calculate_melons(k, directions_lengths)
    print(result)


# 연도 계산
"""
준규가 사는 나라는 우리가 사용하는 연도와 다른 방식을 이용한다. 
준규가 사는 나라에서는 수 3개를 이용해서 연도를 나타낸다. 각각의 수는 지구, 태양, 그리고 달을 나타낸다.
지구를 나타내는 수를 E, 태양을 나타내는 수를 S, 달을 나타내는 수를 M이라고 했을 때, 이 세 수는 서로 다른 범위를 가진다.
(1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)

우리가 알고있는 1년은 준규가 살고있는 나라에서는 1 1 1로 나타낼 수 있다.
1년이 지날 때마다, 세 수는 모두 1씩 증가한다. 만약, 어떤 수가 범위를 넘어가는 경우에는 1이 된다.
예를 들어, 15년은 15 15 15로 나타낼 수 있다. 하지만, 1년이 지나서 16년이 되면 16 16 16이 아니라 1 16 16이 된다. 
이유는 1 ≤ E ≤ 15 라서 범위를 넘어가기 때문이다.
E, S, M이 주어졌고, 1년이 준규가 사는 나라에서 1 1 1일때, 준규가 사는 나라에서 E S M이 우리가 알고 있는 연도로 몇 년인지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 세 수 E, S, M이 주어진다. 문제에 나와있는 범위를 지키는 입력만 주어진다.
출력
첫째 줄에 E S M으로 표시되는 가장 빠른 연도를 출력한다. 1 1 1은 항상 1이기 때문에, 정답이 음수가 나오는 경우는 없다.

예제 입력 1 
1 16 16
예제 출력 1 
16
예제 입력 2 
1 1 1
예제 출력 2 
1
예제 입력 3 
1 2 3
예제 출력 3 
5266
"""
# 풀이 

def find_year(e, s, m):
    year = 1
    while True:
        # Check if the year matches the given E, S, M values
        if (year - 1) % 15 + 1 == e and (year - 1) % 28 + 1 == s and (year - 1) % 19 + 1 == m:
            return year
        year += 1

# Main logic
if __name__ == "__main__":
    # Input values
    e, s, m = map(int, input().split())

    # Calculate the result
    result = find_year(e, s, m)

    # Print the result
    print(result)

# 집합
"""
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.

입력
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

출력
check 연산이 주어질때마다, 결과를 출력한다.
"""
# 풀이

def process_commands(commands):
    S = set()
    results = []

    for command in commands:
        if command[0] == "add":
            S.add(command[1])
        elif command[0] == "remove":
            S.discard(command[1])  # discard avoids KeyError if element is not in the set
        elif command[0] == "check":
            results.append(1 if command[1] in S else 0)
        elif command[0] == "toggle":
            if command[1] in S:
                S.remove(command[1])
            else:
                S.add(command[1])
        elif command[0] == "all":
            S = set(range(1, 21))
        elif command[0] == "empty":
            S.clear()

    return results

# Main logic
if __name__ == "__main__":
    M = int(input())
    commands = []

    for _ in range(M):
        parts = input().split()
        if len(parts) == 2:
            commands.append((parts[0], int(parts[1])))
        else:
            commands.append((parts[0],))

    results = process_commands(commands)

    if results:
        print("\n".join(map(str, results)))


# 카드게임
"""
카드는 빨간색, 파란색, 노란색, 녹색의 네 가지 색이 있고, 색깔별로 1부터 9까지 숫자가 쓰여진 카드가 9장씩 있다. 카드는 모두 36(=4x9)장이다.
근우가 배운 카드 게임은 36장의 카드에서 5장을 뽑고, 아래와 같은 규칙으로 정수를 계산하는 것이다.
각 카드는 다음과 같이 나타낸다. 카드의 색깔은 영어 대문자 R, B, Y, G로 나타내는데, R은 빨간색, B는 파란색, Y는 노란색, G는 녹색을 뜻한다. 
예를 들어서 Y8은 노란색 8을 나타내고, B5는 파란색 5를 나타낸다.

<점수를 정하는 규칙>
1.카드 5장이 모두 같은 색이면서 숫자가 연속적일 때, 점수는 가장 높은 숫자에 900을 더한다. 예를 들어, 카드가 Y4, Y3, Y2, Y5, Y6 일 때 점수는 906(=6+900)점이다.
2.카드 5장 중 4장의 숫자가 같을 때 점수는 같은 숫자에 800을 더한다. 예를 들어, 카드가 B3, R3, B7, Y3, G3 일 때 점수는 803(=3+800)점이다.
3.카드 5장 중 3장의 숫자가 같고 나머지 2장도 숫자가 같을 때 점수는 3장이 같은 숫자에 10을 곱하고 2장이 같은 숫자를 더한 다음 700을 더한다. 예를 들어, 카드가 R5, Y5, G7, B5, Y7 일 때 점수는 757(=5x10+7+700)점이다.
4.5장의 카드 색깔이 모두 같을 때 점수는 가장 높은 숫자에 600을 더한다. 예를 들어, 카드가 Y3, Y4, Y8, Y6, Y7 일 때 점수는 608(=8+600)점이다.
5.카드 5장의 숫자가 연속적일 때 점수는 가장 높은 숫자에 500을 더한다. 예를 들어 R7, R8, G9, Y6, B5 일 때 점수는 509(=9+500)점이다.
6.카드 5장 중 3장의 숫자가 같을 때 점수는 같은 숫자에 400을 더한다. 예를 들어 R7, Y7, R2, G7, R5 일 때 점수는 407(=7+400)점이다.
7.카드 5장 중 2장의 숫자가 같고 또 다른 2장의 숫자가 같을 때 점수는 같은 숫자 중 큰 숫자에 10을 곱하고 같은 숫자 중 작은 숫자를 더한 다음 300을 더한다. 예를 들어, R5, Y5, Y4, G9, B4 일 때 점수는 354(=5X10+4+300)점이다.
8.카드 5장 중 2장의 숫자가 같을 때 점수는 같은 숫자에 200을 더한다. 예를 들어, R5, Y2, B5, B3, G4 일 때 점수는 205(=5+200)점이다.
9.위의 어떤 경우에도 해당하지 않을 때 점수는 가장 큰 숫자에 100을 더한다. 예를 들어, R1, R2, B4, B8, Y5 일 때 점수는 108(=8+100)점이다.
10.입력으로 카드 5장이 주어질 때, 카드 게임의 점수를 구하는 프로그램을 작성하시오. 두 가지 이상의 규칙을 적용할 수 있는 경우에는 가장 높은 점수가 카드 게임의 점수이다.

입력
첫째 줄부터 다섯째 줄까지 한 줄에 카드 하나씩 입력된다. 카드의 색깔과 숫자 사이에는 빈 칸이 하나 있다.
출력
한 줄에 카드의 점수를 출력한다.

예제 입력 1 
B 3
B 7
R 1
B 2
Y 7
예제 출력 1 
207
"""
# 풀이


def calculate_card_score(cards):
    colors = [card[0] for card in cards]  # Extract colors
    numbers = [int(card[1]) for card in cards]  # Extract numbers

    # Count occurrences of colors and numbers without Counter
    color_count = {}
    number_count = {}

    for color in colors:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    for number in numbers:
        if number in number_count:
            number_count[number] += 1
        else:
            number_count[number] = 1

    # Sort numbers for sequential check
    numbers.sort()

    # Rule 1: All same color and sequential numbers
    if len(color_count) == 1 and all(numbers[i] + 1 == numbers[i + 1] for i in range(4)):
        return numbers[-1] + 900

    # Rule 2: Four of a kind
    if 4 in number_count.values():
        for num, count in number_count.items():
            if count == 4:
                return num + 800

    # Rule 3: Full house (3 of one kind and 2 of another)
    if sorted(number_count.values()) == [2, 3]:
        three_of_a_kind = None
        pair = None
        for num, count in number_count.items():
            if count == 3:
                three_of_a_kind = num
            elif count == 2:
                pair = num
        return three_of_a_kind * 10 + pair + 700

    # Rule 4: All same color
    if len(color_count) == 1:
        return numbers[-1] + 600

    # Rule 5: Sequential numbers
    if all(numbers[i] + 1 == numbers[i + 1] for i in range(4)):
        return numbers[-1] + 500

    # Rule 6: Three of a kind
    if 3 in number_count.values():
        for num, count in number_count.items():
            if count == 3:
                return num + 400

    # Rule 7: Two pairs
    if list(number_count.values()).count(2) == 2:
        pairs = []
        for num, count in number_count.items():
            if count == 2:
                pairs.append(num)
        return max(pairs) * 10 + min(pairs) + 300

    # Rule 8: One pair
    if 2 in number_count.values():
        for num, count in number_count.items():
            if count == 2:
                return num + 200

    # Rule 9: Highest number
    return numbers[-1] + 100

# Main logic
if __name__ == "__main__":
    cards = [input().split() for _ in range(5)]  # Read input
    score = calculate_card_score(cards)
    print(score)

# olympic ranking
"""
버블 정렬
1.금메달 수가 더 많은 나라
2.금메달 수가 같으면, 은메달 수가 더 많은 나라
3. 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라
각 국가는 1부터 N 사이의 정수로 표현된다. 한 국가의 등수는 (자신보다 더 잘한 나라 수) + 1로 정의된다. 만약 두 나라가 금, 은, 동메달 수가 모두 같다면 두 나라의 등수는 같다. 
예를 들어, 1번 국가가 금메달 1개, 은메달 1개를 얻었고, 2번 국가와 3번 국가가 모두 은메달 1개를 얻었으며, 4번 국가는 메달을 얻지 못하였다면, 
1번 국가가 1등, 2번 국가와 3번 국가가 공동 2등, 4번 국가가 4등이 된다. 이 경우 3등은 없다.
각 국가의 금, 은, 동메달 정보를 입력받아서, 어느 국가가 몇 등을 했는지 알려주는 프로그램을 작성하시오.

입력
입력의 첫 줄은 국가의 수 N(1 ≤ N ≤ 1,000)과 등수를 알고 싶은 국가 K(1 ≤ K ≤ N)가 빈칸을 사이에 두고 주어진다. 
각 국가는 1부터 N 사이의 정수로 표현된다. 이후 N개의 각 줄에는 차례대로 각 국가를 나타내는 정수와 이 국가가 얻은 금, 은, 동메달의 수가 빈칸을 사이에 두고 주어진다. 
전체 메달 수의 총합은 1,000,000 이하이다.
출력
출력은 단 한 줄이며, 입력받은 국가 K의 등수를 하나의 정수로 출력한다. 등수는 반드시 문제에서 정의된 방식을 따라야 한다.

예제 입력 1 
4 3
1 1 2 0
2 0 1 0
3 0 1 0
4 0 0 1
예제 출력 1 
2
"""
# 풀이

def find_rank(n, k, countries):
    # Manual sorting based on the rules
    for i in range(n - 1):
        for j in range(n - 1 - i):
            # Compare gold medals first, then silver, then bronze
            if (countries[j][1] < countries[j + 1][1] or
                (countries[j][1] == countries[j + 1][1] and countries[j][2] < countries[j + 1][2]) or
                (countries[j][1] == countries[j + 1][1] and countries[j][2] == countries[j + 1][2] and countries[j][3] < countries[j + 1][3])):
                # Swap the two countries to sort
                countries[j], countries[j + 1] = countries[j + 1], countries[j]

    # Assign ranks to all countries
    ranks = [0] * n  # Array to store ranks of each country
    rank = 1
    for i in range(n):
        if i > 0 and (countries[i][1:] != countries[i - 1][1:]):
            rank = i + 1
        ranks[countries[i][0]] = rank  # Assign rank to the corresponding country ID

    return ranks[k]  # Return the rank of the target country

# Main logic
if __name__ == "__main__":
    n, k = map(int, input().split())  # Number of countries and target country
    countries = []
    for _ in range(n):
        country = list(map(int, input().split()))  # Read country data (ID, gold, silver, bronze)
        countries.append(country)

    result = find_rank(n, k, countries)
    print(result)


# 줄에서 숫자 찾기
"""
선생님이 상근이에게 준 종이에는 숫자와 알파벳 소문자로 되어있는 글자가 N줄있다. 
상근이는 여기서 숫자를 모두 찾은 뒤, 이 숫자를 비내림차순으로 정리해야한다. 숫자의 앞에 0이 있는 경우에는 정리하면서 생략할 수 있다.
글자를 살펴보다가 숫자가 나오는 경우에는, 가능한 가장 큰 숫자를 찾아야 한다. 즉, 모든 숫자의 앞과 뒤에 문자가 있거나, 줄의 시작 또는 끝이어야 한다.

예를 들어, 01a2b3456cde478에서 숫자를 찾으면 1, 2, 3456, 478이다.
선생님이 준 종이의 내용이 주어졌을 때, 상근이의 숙제를 대신하는 프로그램을 작성하시오.

입력
첫째 줄에 종이의 줄의 개수 N이 주어진다. (1 ≤ N ≤ 100)
다음 N개의 줄에는 각 줄의 내용이 주어진다. 각 줄은 최대 100글자이고, 항상 알파벳 소문자와 숫자로만 이루어져 있다.

출력
종이에서 찾은 숫자의 개수를 M이라고 하면, 출력은 M줄로 이루어져야 한다. 각 줄에는 종이에서 찾은 숫자를 하나씩 출력해야 한다. 이때, 오름차순으로 출력해야 한다.

예제 입력 1 
2
lo3za4
01
예제 출력 1 
1
3
4
"""
# 풀이

def find_and_sort_numbers(lines):
    numbers = []

    # 각 줄에서 숫자를 추출
    for line in lines:
        num = ""
        for char in line:
            if '0' <= char <= '9':
                num += char
            else:
                if num:
                    numbers.append(int(num))
                    num = ""
        if num:
            numbers.append(int(num))

    # 비내림차순으로 정렬
    numbers.sort()

    return numbers

# 입력 받기
n = int(input())  # 줄의 개수
lines = [input().strip() for _ in range(n)]

# 함수 호출 및 결과 출력
result = find_and_sort_numbers(lines)
for num in result:
    print(num)

# 비밀번호 발음하기
"""
1.모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
2.모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
3.같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
이 규칙은 완벽하지 않다;우리에게 친숙하거나 발음이 쉬운 단어 중에서도 품질이 낮게 평가되는 경우가 많이 있다.

입력
입력은 여러개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 테스트할 패스워드가 주어진다.
마지막 테스트 케이스는 end이며, 패스워드는 한글자 이상 20글자 이하의 문자열이다. 또한 패스워드는 대문자를 포함하지 않는다.

출력
각 테스트 케이스를 '예제 출력'의 형태에 기반하여 품질을 평가하여라.

예제 입력 1 
a
tv
ptoui
bontres
zoggax
wiinq
eep
houctuh
end
예제 출력 1 
<a> is acceptable.
<tv> is not acceptable.
<ptoui> is not acceptable.
<bontres> is not acceptable.
<zoggax> is not acceptable.
<wiinq> is not acceptable.
<eep> is acceptable.
<houctuh> is acceptable.
"""

def is_acceptable(password):
    vowels = "aeiou"
    
    # 규칙 1: 모음 하나 이상 포함
    has_vowel = any(char in vowels for char in password)
    if not has_vowel:
        return False

    # 규칙 2: 모음 3개 또는 자음 3개 연속 불가
    for i in range(len(password) - 2):
        if (password[i] in vowels and password[i + 1] in vowels and password[i + 2] in vowels) or \
           (password[i] not in vowels and password[i + 1] not in vowels and password[i + 2] not in vowels):
            return False

    # 규칙 3: 같은 글자 연속 두번 불가 ("ee"와 "oo"는 허용)
    for i in range(len(password) - 1):
        if password[i] == password[i + 1] and (password[i] != 'e' and password[i] != 'o'):
            return False

    return True

# 입력 및 결과 처리
while True:
    password = input().strip()
    if password == "end":
        break

    if is_acceptable(password):
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")
    
# 기상캐스터
"""
JOI시는 남북방향이 H 킬로미터, 동서방향이 W 킬로미터인 직사각형 모양이다. 
JOI시는 가로와 세로의 길이가 1킬로미터인 H × W 개의 작은 구역들로 나뉘어 있다. 북쪽으로부터 i 번째, 서쪽으로부터 j 번째에 있는 구역을 (i, j) 로 표시한다.
각 구역의 하늘에는 구름이 있을 수도, 없을 수도 있다. 모든 구름은 1분이 지날 때마다 1킬로미터씩 동쪽으로 이동한다.
오늘은 날씨가 정말 좋기 때문에 JOI시의 외부에서 구름이 이동해 오는 경우는 없다.
지금 각 구역의 하늘에 구름이 있는지 없는지를 알고 있다. 
각 구역에 대해서 지금부터 몇 분뒤 처음으로 하늘에 구름이 오는지를 구하여라.

입력
입력은 1 + H 행으로 주어진다.
첫 번째 행에는 정수 H, W (1 ≦ H ≦ 100, 1 ≦ W ≦ 100) 가 공백을 사이에 주고 주어진다. 이것은 JOI시가 H × W 개의 작은 구역으로 나뉘어 있다는 것을 의미한다.
이어진 H 개의 행의 i번째 행 (1 ≦ i ≦ H) 에는 W문자의 문자열이 주어진다. W 개의 문자 중 j번째 문자 (1 ≦ j ≦ W) 는, 
구역 (i, j) 에 지금 구름이 떠 있는지 아닌지를 나타낸다. 구름이 있는 경우에는 영어 소문자 'c' 가, 구름이 없는 경우에는 문자 '.' 가 주어진다.

출력
출력은 H 행으로, 각 행에는 공백으로 구분된 W 개의 정수를 출력한다. 출력의 i 번째 행 j 번째 정수 (1 ≦ i ≦ H, 1 ≦ j ≦ W) 는, 
지금부터 몇 분후에 처음으로 구역 (i, j) 에 구름이 뜨는지를 표시한다. 단, 처음부터 구역 (i, j) 에 구름이 떠 있었던 경우에는 0을, 
몇 분이 지나도 구름이 뜨지 않을 경우에는 -1을 출력한다.

예제 입력 1 
3 4
c..c
..c.
....
예제 출력 1 
0 1 2 0
-1 -1 0 1
-1 -1 -1 -1
"""
def calculate_cloud_time(H, W, grid):
    result = []

    for i in range(H):
        row_result = []
        last_cloud = -1  # 마지막 구름이 등장한 위치

        for j in range(W):
            if grid[i][j] == 'c':
                last_cloud = j
                row_result.append(0)  # 구름이 현재 위치에 있음
            else:
                if last_cloud == -1:
                    row_result.append(-1)  # 구름이 도달하지 않음
                else:
                    row_result.append(j - last_cloud)  # 구름이 도달하는 시간 계산

        result.append(row_result)

    return result

# 입력 처리
H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# 결과 계산
result = calculate_cloud_time(H, W, grid)

# 결과 출력
for row in result:
    print(" ".join(map(str, row)))

# 영화감독 숌
"""
666은 종말을 나타내는 수라고 한다. 따라서, 많은 블록버스터 영화에서는 666이 들어간 제목을 많이 사용한다.
종말의 수란 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수를 말한다. 
제일 작은 종말의 수는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... 이다. 
따라서, 숌은 첫 번째 영화의 제목은 "세상의 종말 666", 두 번째 영화의 제목은 "세상의 종말 1666"와 같이 이름을 지을 것이다. 
일반화해서 생각하면, N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 수) 와 같다.
숌이 만든 N번째 영화의 제목에 들어간 수를 출력하는 프로그램을 작성하시오. 

입력
첫째 줄에 N이 주어진다. N은 10,000보다 작거나 같은 자연수이다.
출력
첫째 줄에 N번째 영화의 제목에 들어간 수를 출력한다.
예제 입력 1 
2
예제 출력 1 
1666
예제 입력 2 
3
예제 출력 2 
2666
예제 입력 3 
6
예제 출력 3 
5666 
"""
class EndOfWorldNumber:
    def __init__(self):
        self.numbers = []  # 종말의 수를 저장할 리스트

    def generate_numbers(self, n):
        """
        N번째 종말의 수를 생성한다.
        """
        number = 666  # 첫 번째 종말의 수
        count = 0     # 종말의 수 개수를 센다

        while count < n:
            # '666'이 포함된 숫자면 리스트에 추가
            if '666' in str(number):
                self.numbers.append(number)
                count += 1
            number += 1  # 다음 숫자 확인

    def get_nth_number(self, n):
        """
        N번째 종말의 수를 반환한다.
        """
        if len(self.numbers) < n:
            self.generate_numbers(n)
        return self.numbers[n - 1]

# 사용 예시
if __name__ == "__main__":
    n = int(input("Enter the N value: "))
    eow_number = EndOfWorldNumber()
    result = eow_number.get_nth_number(n)
    print(result)

# 수찾기
"""
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

예제 입력 1 
5
4 1 5 2 3
5
1 3 7 9 5
예제 출력 1 
1
1
0
0
1
"""
class NumberExistenceChecker:
    def __init__(self, numbers):
        """
        초기화: 입력된 리스트를 집합으로 변환해 저장.
        """
        self.number_set = set(numbers)

    def check_numbers(self, queries):
        """
        주어진 쿼리 리스트에서 각 숫자의 존재 여부를 확인.
        """
        results = []
        for query in queries:
            if query in self.number_set:
                results.append(1)
            else:
                results.append(0)
        return results

# 실행 코드
if __name__ == "__main__":
    # 입력 파싱
    N = int(input("Enter the number of elements in the list: "))
    numbers = list(map(int, input("Enter the numbers separated by spaces: ").split()))
    M = int(input("Enter the number of queries: "))
    queries = list(map(int, input("Enter the queries separated by spaces: ").split()))

    # 클래스 생성 및 결과 확인
    checker = NumberExistenceChecker(numbers)
    results = checker.check_numbers(queries)

    # 결과 출력
    print("\n".join(map(str, results)))

# 퇴사 -> dfs
"""
상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.
오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.
백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.
각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.
N = 7인 경우에 다음과 같은 상담 일정표를 보자.

 	1일	2일	3일	4일	5일	6일	7일
Ti	3	5	1	1	2	4	2
Pi	10	20	10	20	15	40	200

1일에 잡혀있는 상담은 총 3일이 걸리며, 상담했을 때 받을 수 있는 금액은 10이다. 5일에 잡혀있는 상담은 총 2일이 걸리며, 받을 수 있는 금액은 15이다.
상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다. 
예를 들어서 1일에 상담을 하게 되면, 2일, 3일에 있는 상담은 할 수 없게 된다. 2일에 있는 상담을 하게 되면, 3, 4, 5, 6일에 잡혀있는 상담은 할 수 없다.
또한, N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다.
퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 이때의 이익은 10+20+15=45이다.
상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

출력
첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.

예제 입력 1 
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
예제 출력 1 
45
"""
class ConsultingScheduler:
    def __init__(self, n, schedule):
        """
        초기화: 상담 일정을 저장
        :param n: 남은 날짜 수
        :param schedule: 상담 일정 (Ti, Pi) 리스트
        """
        self.n = n
        self.schedule = schedule
        self.max_profit = 0  # 최대 수익 저장

    def calculate_max_profit(self):
        """
        최대 수익 계산을 위한 메인 함수
        """
        self._dfs(0, 0)
        return self.max_profit

    def _dfs(self, day, profit):
        """
        DFS를 이용한 백트래킹으로 최대 수익 계산
        :param day: 현재 날짜
        :param profit: 현재까지의 수익
        """
        # 날짜가 범위를 넘어가면 최대 수익 갱신
        if day >= self.n:
            self.max_profit = max(self.max_profit, profit)
            return

        # 현재 상담을 선택하지 않는 경우
        self._dfs(day + 1, profit)

        # 현재 상담을 선택하는 경우 (날짜 초과 방지)
        if day + self.schedule[day][0] <= self.n:
            self._dfs(day + self.schedule[day][0], profit + self.schedule[day][1])

# 실행 코드
if __name__ == "__main__":
    # 입력 파싱
    n = int(input("Enter the number of days: "))
    schedule = []
    for _ in range(n):
        t, p = map(int, input("Enter Ti and Pi separated by space: ").split())
        schedule.append((t, p))

    # 클래스 생성 및 최대 수익 계산
    scheduler = ConsultingScheduler(n, schedule)
    max_profit = scheduler.calculate_max_profit()

    # 결과 출력
    print(max_profit)

# 펠린드롬 만들기
"""
임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데, 임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.
임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성하시오.

입력
첫째 줄에 임한수의 영어 이름이 있다. 알파벳 대문자로만 된 최대 50글자이다.
출력
첫째 줄에 문제의 정답을 출력한다. 만약 불가능할 때는 "I'm Sorry Hansoo"를 출력한다. 
정답이 여러 개일 경우에는 사전순으로 앞서는 것을 출력한다.

예제 입력 1 
AABB
예제 출력 1 
ABBA
"""
class PalindromeMaker:
    def __init__(self, name):
        """
        초기화: 입력된 이름을 저장하고, 알파벳 빈도를 계산합니다.
        """
        self.name = name
        self.char_count = {}
        for char in name:
            if char in self.char_count:
                self.char_count[char] += 1
            else:
                self.char_count[char] = 1

    def make_palindrome(self):
        """
        팰린드롬을 생성하거나 불가능할 경우 에러 메시지를 반환합니다.
        """
        odd_count = 0  # 홀수 개수의 문자를 카운트
        middle_char = ""  # 팰린드롬의 가운데에 올 문자
        half_palindrome = []

        # 각 문자의 빈도를 확인
        for char in sorted(self.char_count):  # 사전순으로 처리
            count = self.char_count[char]
            if count % 2 != 0:
                odd_count += 1
                middle_char = char

            # 홀수 문자가 2개 이상이면 팰린드롬 생성 불가
            if odd_count > 1:
                return "I'm Sorry Hansoo"

            # 절반을 구성할 문자 추가
            half_palindrome.extend(char * (count // 2))

        # 팰린드롬 생성
        half_palindrome = "".join(half_palindrome)
        return half_palindrome + middle_char + half_palindrome[::-1]

# 실행 코드
if __name__ == "__main__":
    name = input("Enter the name: ").strip()
    palindrome_maker = PalindromeMaker(name)
    result = palindrome_maker.make_palindrome()
    print(result)

# 주몽 -> 투 포인터 이용
"""
갑옷을 만드는 재료들은 각각 고유한 번호를 가지고 있다.
갑옷은 두 개의 재료로 만드는데 두 재료의 고유한 번호를 합쳐서 M(1 ≤ M ≤ 10,000,000)이 되면 갑옷이 만들어 지게 된다.
야철대장은 자신이 만들고 있는 재료를 가지고 갑옷을 몇 개나 만들 수 있는지 궁금해졌다. 
이러한 궁금증을 풀어 주기 위하여 N(1 ≤ N ≤ 15,000) 개의 재료와 M이 주어졌을 때 몇 개의 갑옷을 만들 수 있는지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 재료의 개수 N(1 ≤ N ≤ 15,000)이 주어진다. 
그리고 두 번째 줄에는 갑옷을 만드는데 필요한 수 M(1 ≤ M ≤ 10,000,000) 주어진다. 그
리고 마지막으로 셋째 줄에는 N개의 재료들이 가진 고유한 번호들이 공백을 사이에 두고 주어진다. 고유한 번호는 100,000보다 작거나 같은 자연수이다.
출력
첫째 줄에 갑옷을 만들 수 있는 개수를 출력한다.

예제 입력 1 
6
9
2 7 4 1 5 3
예제 출력 1 
2
"""

class ArmorCombinations:
    def __init__(self, n, m, materials):
        """
        초기화
        :param n: 재료의 개수
        :param m: 목표 합
        :param materials: 재료 리스트
        """
        self.n = n
        self.m = m
        self.materials = sorted(materials)  # 재료를 정렬

    def count_combinations(self):
        """
        투 포인터를 이용하여 가능한 갑옷의 조합 개수를 계산
        :return: 갑옷의 조합 개수
        """
        left, right = 0, self.n - 1
        count = 0

        while left < right:
            current_sum = self.materials[left] + self.materials[right]

            if current_sum == self.m:
                count += 1
                left += 1
                right -= 1
            elif current_sum < self.m:
                left += 1
            else:
                right -= 1

        return count

# 실행 코드
if __name__ == "__main__":
    n = int(input("Enter the number of materials: "))
    m = int(input("Enter the target sum M: "))
    materials = list(map(int, input("Enter the materials separated by spaces: ").split()))

    # 클래스 생성 및 조합 계산
    armor_combinations = ArmorCombinations(n, m, materials)
    result = armor_combinations.count_combinations()

    # 결과 출력
    print(result)

# 좋은 단어
""" 안타깝게도 자는 동안 키보드가 잘못 눌려서 보고서의 모든 글자가 A와 B로 바뀌어 버렸다! 
그래서 평석이는 보고서 작성을 때려치우고 보고서에서 '좋은 단어'나 세보기로 마음 먹었다.
평석이는 단어 위로 아치형 곡선을 그어 같은 글자끼리(A는 A끼리, B는 B끼리) 쌍을 짓기로 하였다. 
만약 선끼리 교차하지 않으면서 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝 지을수 있다면, 그 단어는 '좋은 단어'이다.
평석이가 '좋은 단어' 개수를 세는 것을 도와주자.

입력
첫째 줄에 단어의 수 N이 주어진다. (1 ≤ N ≤ 100)
다음 N개 줄에는 A와 B로만 이루어진 단어가 한 줄에 하나씩 주어진다. 단어의 길이는 2와 100,000사이이며, 모든 단어 길이의 합은 1,000,000을 넘지 않는다.

출력
첫째 줄에 좋은 단어의 수를 출력한다.

예제 입력 1 
3
ABAB
AABB
ABBA
예제 출력 1 
2
"""
class GoodWordChecker:
    def __init__(self):
        self.good_word_count = 0

    def is_good_word(self, word):
        stack = []
        for char in word:
            if stack and stack[-1] == char:
                stack.pop()  # 짝을 지으면 제거
            else:
                stack.append(char)  # 짝이 안 맞으면 추가

        # 스택이 비어 있으면 좋은 단어
        return len(stack) == 0

    def count_good_words(self, words):
        for word in words:
            if self.is_good_word(word):
                self.good_word_count += 1
        return self.good_word_count


# 실행 코드
if __name__ == "__main__":
    n = int(input("Enter the number of words: "))
    words = [input("Enter a word: ").strip() for _ in range(n)]

    checker = GoodWordChecker()
    result = checker.count_good_words(words)
    print(result)

# 교수가 된 현우
"""
그러나 학생들에게 크나큰 기대를 품고 첫 수업에 들어갔던 현우는 아무도 외판원 순회 문제(Traveling Salesman Problem, TSP)를 풀지 못하는 것을 보고 낙심하였다.
그 와중에 학생 남규는 TSP를 완전탐색으로 풀려고 하였고, 현우는 그걸 보고 경악을 금치 못한다. 
왜냐면 TSP를 완전탐색으로 풀려면 O(N!)의 시간이 소모되는데, 이는 경악을 금치 못할 시간이기 때문이다.
그러나 남규는 O(N!)이 왜 큰지도 잘 모른다.
그래서 현우는 더더욱 경악을 금치 못하고, N!이 얼마나 큰지 대략적으로나마 알려주기 위해, 자연수 N이 주어지면 N!의 오른쪽 끝에 있는 0의 개수를 알려주기로 하였다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어지고, 이어서 T개의 줄에 정수 N이 주어진다(1 <= N <= 1000000000).
출력
각 줄마다 N!의 오른쪽 끝에 있는 0의 개수를 출력한다.

예제 입력 1 
6
3
60
100
1024
23456
8735373
예제 출력 1 
0
14
24
253
5861
2183837
"""
class FactorialTrailingZeroes:
    def __init__(self, test_cases):
        self.test_cases = test_cases

    def count_trailing_zeroes(self, n):
        count = 0
        power_of_five = 5
        while n >= power_of_five:
            count += n // power_of_five
            power_of_five *= 5
        return count

    def solve(self):
        results = []
        for n in self.test_cases:
            results.append(self.count_trailing_zeroes(n))
        return results


# 실행 코드
if __name__ == "__main__":
    t = int(input("Enter the number of test cases: "))
    test_cases = [int(input(f"Enter test case {i + 1}: ")) for i in range(t)]

    solver = FactorialTrailingZeroes(test_cases)
    results = solver.solve()

    for result in results:
        print(result)
    
# 괄호
"""
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 
그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 
한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 
그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 
예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 
여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

입력
입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 
각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 
출력
출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 

예제 입력 1 
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
예제 출력 1 
NO
NO
YES
NO
YES
NO
"""
class ParenthesisChecker:
    def __init__(self, test_cases):
        self.test_cases = test_cases

    def is_vps(self, ps):
        stack = []
        for char in ps:
            if char == '(':
                stack.append(char)  # 여는 괄호 추가
            elif char == ')':
                if stack: # 스택에 요소가 하나라도 있을때 true
                    stack.pop()  # 짝이 맞는 경우 제거
                else:
                    return "NO"  # 스택이 비어 있으면 NO
        # 모든 문자열을 탐색한 뒤 스택이 비어 있으면 YES
        return "YES" if not stack else "NO"

    def solve(self):
        results = []
        for ps in self.test_cases:
            results.append(self.is_vps(ps))
        return results


# 실행 코드
if __name__ == "__main__":
    t = int(input("Enter the number of test cases: "))
    test_cases = [input(f"Enter test case {i + 1}: ").strip() for i in range(t)]

    checker = ParenthesisChecker(test_cases)
    results = checker.solve()

    for result in results:
        print(result)

# 균형잡힌 세상
"""
정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.
문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.

입력
각 문자열은 마지막 글자를 제외하고 영문 알파벳, 공백, 소괄호("( )"), 대괄호("[ ]")로 이루어져 있으며, 온점(".")으로 끝나고, 길이는 100글자보다 작거나 같다.
입력의 종료조건으로 맨 마지막에 온점 하나(".")가 들어온다.
출력
각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.

예제 입력 1 
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.
예제 출력 1 
yes
yes
no
no
no
yes
yes
"""

class BalancedStringChecker:
    def __init__(self):
        self.results = []

    def is_balanced(self, string):
        stack = []
        for char in string:
            if char in "([":  # 여는 괄호
                stack.append(char)
            elif char == ")":  # 닫는 소괄호
                if not stack or stack[-1] != "(":
                    return "no"
                stack.pop()
            elif char == "]":  # 닫는 대괄호
                if not stack or stack[-1] != "[":
                    return "no"
                stack.pop()
        return "yes" if not stack else "no"

    def solve(self, lines):
        for line in lines:
            if line == ".":
                break
            self.results.append(self.is_balanced(line))
        return self.results


# 실행 코드
if __name__ == "__main__":
    lines = []
    while True:
        line = input().strip()
        if line == ".":
            break
        lines.append(line)

    checker = BalancedStringChecker()
    results = checker.solve(lines)

    for result in results:
        print(result)
    
# 스택 수열
"""
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 
스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.
1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다.

입력
첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.
출력
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.

예제 입력 1 
8
4
3
6
8
7
5
2
1
예제 출력 1 
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-
예제 입력 2 
5
1
2
5
3
4
예제 출력 2 
NO
"""
class StackSequence:
    def __init__(self, n, sequence):
        """
        초기화
        :param n: 수열의 크기
        :param sequence: 주어진 수열
        """
        self.n = n
        self.sequence = sequence

    def can_form_sequence(self):
        """
        스택 연산을 사용하여 주어진 수열을 만들 수 있는지 판단
        :return: 연산 결과 리스트 ("NO" 또는 연산 순서)
        """
        stack = []
        result = []
        current = 1

        for target in self.sequence:
            # target까지 스택에 push
            while current <= target:
                stack.append(current)
                result.append('+')
                current += 1

            # 스택의 최상단 값이 target과 같은 경우 pop
            if stack and stack[-1] == target:
                stack.pop()
                result.append('-')
            else:
                # 스택의 최상단 값이 target보다 크다면 불가능
                return ["NO"]

        return result

# 실행 코드
if __name__ == "__main__":
    n = int(input("Enter the size of the sequence: "))
    sequence = [int(input()) for _ in range(n)]

    stack_sequence = StackSequence(n, sequence)
    result = stack_sequence.can_form_sequence()

    for r in result:
        print(r)

# 프린터 큐
"""
여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다.
여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 
하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.
현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.
여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다.
예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.

입력
첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.
테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 
이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.ㄴ
출력
각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.

예제 입력 1 
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
예제 출력 1 
1
2
5
"""
class PrinterQueue:
    def __init__(self, priorities, target_index):
        self.queue = [(priorities[i], i) for i in range(len(priorities))]
        self.target_index = target_index

    def print_order(self):
        print_count = 0

        while self.queue:
            # Check the first document in the queue
            current = self.queue.pop(0)
            if any(current[0] < other[0] for other in self.queue):
                # If there's a higher priority document, re-add current to the queue
                self.queue.append(current)
            else:
                # Print the current document
                print_count += 1
                if current[1] == self.target_index:
                    return print_count

if __name__ == "__main__":
    test_cases = int(input())
    results = []

    for _ in range(test_cases):
        n, m = map(int, input().split())
        priorities = list(map(int, input().split()))
        printer = PrinterQueue(priorities, m)
        results.append(printer.print_order())

    # Output results
    for result in results:
        print(result)

# 키로거
"""창영이는 강산이의 비밀번호를 훔치기 위해서 강산이가 사용하는 컴퓨터에 키로거를 설치했다. 며칠을 기다린 끝에 창영이는 강산이가 비밀번호 창에 입력하는 글자를 얻어냈다.
키로거는 사용자가 키보드를 누른 명령을 모두 기록한다. 따라서, 강산이가 비밀번호를 입력할 때, 화살표나 백스페이스를 입력해도 정확한 비밀번호를 알아낼 수 있다. 
강산이가 비밀번호 창에서 입력한 키가 주어졌을 때, 강산이의 비밀번호를 알아내는 프로그램을 작성하시오. 
강산이는 키보드로 입력한 키는 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표이다.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한줄로 이루어져 있고, 강산이가 입력한 순서대로 길이가 L인 문자열이 주어진다. (1 ≤ L ≤ 1,000,000) 
강산이가 백스페이스를 입력했다면, '-'가 주어진다. 이때 커서의 바로 앞에 글자가 존재한다면, 그 글자를 지운다. 
화살표의 입력은 '<'와 '>'로 주어진다. 이때는 커서의 위치를 움직일 수 있다면, 왼쪽 또는 오른쪽으로 1만큼 움직인다. 
나머지 문자는 비밀번호의 일부이다. 물론, 나중에 백스페이스를 통해서 지울 수는 있다. 
만약 커서의 위치가 줄의 마지막이 아니라면, 커서 및 커서 오른쪽에 있는 모든 문자는 오른쪽으로 한 칸 이동한다.
출력
각 테스트 케이스에 대해서, 강산이의 비밀번호를 출력한다. 비밀번호의 길이는 항상 0보다 크다.

예제 입력 1 
2
<<BP<A>>Cd-
ThIsIsS3Cr3t
예제 출력 1 
BAPC
ThIsIsS3Cr3t
"""
class KeyLogger:
    def __init__(self):
        self.left_stack = []  # 커서 왼쪽에 있는 문자들
        self.right_stack = []  # 커서 오른쪽에 있는 문자들

    def process_key(self, key):
        if key == '-':
            # 백스페이스: 왼쪽 스택에서 마지막 문자 제거 -> stack.pop()는 마지막꺼 제거 
            if self.left_stack:
                self.left_stack.pop()
        elif key == '<':
            # 왼쪽 화살표: 왼쪽 스택의 마지막 문자를 오른쪽 스택으로 이동
            if self.left_stack:
                self.right_stack.append(self.left_stack.pop())
        elif key == '>':
            # 오른쪽 화살표: 오른쪽 스택의 마지막 문자를 왼쪽 스택으로 이동
            if self.right_stack:
                self.left_stack.append(self.right_stack.pop())
        else:
            # 일반 문자: 왼쪽 스택에 추가
            self.left_stack.append(key)

    def get_password(self):
        # 왼쪽 스택 + 오른쪽 스택
        return ''.join(self.left_stack) + ''.join(self.right_stack)

if __name__ == "__main__":
    test_cases = int(input())
    results = []

    for _ in range(test_cases):
        key_sequence = input().strip()
        key_logger = KeyLogger()

        for key in key_sequence:
            key_logger.process_key(key)

        results.append(key_logger.get_password())

    # 출력
    for result in results:
        print(result)

# 죽음의 게임
"""
죽음의 게임의 룰은 간단하다.
게임에 참여하는 N명의 사람들은 원탁에 둘러앉게 된다. 게임을 시작하는 사람은 0번, 그 오른쪽 사람은 1번, 그 오른쪽은 2번, N-1번의 오른쪽 사람은 다시 0번이 된다.
0번이 "신난다! 아싸 재미난다! 아싸 더 게임 오브 데! 스!" 라고 외침과 동시에, 모든 사람들은 각각 테이블에 둘러 앉은 사람들 중 한 명을 지목한다. 
그리고 나서 0번은 임의의 양의 정수 M을 외친다.
그 다음, 0번은 "1"이라고 말한다. 이때 "1"이라고 말한 사람이 지목한 사람은 "2"라고 말하고, "2"라고 말한 사람이 지목한 사람은 "3"이라고 말하고, 같은 방식으로 반복해 M까지 말하게 된다.
이때 마지막으로 M이라고 말한 사람이 지목한 사람은 벌주를 마시게 된다.
새내기에게 벌주를 마시게 하기에는 죄책감이 들었던 영기는 동기인 보성이를 공격하기로 결심했다. 
게임 참여자들간에 지목을 완료한 상태가 주어질때, 보성이가 벌주를 마시기 위해 영기가 불러야 하는 가장 작은 양의 정수 M을 보성이 몰래 귀띔해 주도록 하자.
김영기는 게임을 제안하였기에 자연스럽게 0번이 된다.

입력
첫 번째 줄에 게임에 참여하는 사람의 수 N(3 ≤ N ≤ 150)과 보성이의 번호 K(1 ≤ K ≤ N - 1)가 공백을 두고 주어진다.
두번째 줄부터 N줄에 걸쳐 i(0 ≤ i ≤ N - 1)번 사람이 지목하는 사람의 번호 ai(0 ≤ ai ≤ N - 1)가 주어진다. 자기 자신을 지목하는 경우도 존재할 수 있다.
출력
영기가 말해야 하는 가장 작은 양의 정수 M을 출력한다. 만약 어떤 방법으로도 보성이가 걸리지 않는다면 -1을 출력한다.

예제 입력 1 
5 3
1
3
2
1
4
예제 출력 1 
2 
"""
class GameOfDeath:
    def __init__(self, n, k, targets):
        self.n = n  # 참여자 수
        self.k = k  # 보성이의 번호
        self.targets = targets  # 각 사람이 지목한 대상

    def find_minimum_m(self):
        visited = [False] * self.n  # 방문 여부 확인
        current = 0  # 게임 시작은 0번 사람
        count = 0  # 몇 번째로 호출되었는지 카운트

        while not visited[current]:
            visited[current] = True  # 현재 사람 방문 처리
            count += 1  # 호출 횟수 증가

            # 지목한 사람이 보성이인지 확인
            if self.targets[current] == self.k:
                return count  # 보성이가 걸렸다면 호출 횟수 반환

            # 다음 사람으로 이동
            current = self.targets[current]

        # 사이클이 생겼거나, 보성이가 걸리지 않는 경우
        return -1

if __name__ == "__main__":
    # 입력 처리
    n, k = map(int, input().split())
    targets = [int(input().strip()) for _ in range(n)]

    # 게임 객체 생성
    game = GameOfDeath(n, k, targets)

    # 최소 M값 계산 및 출력
    result = game.find_minimum_m()
    print(result)

# 단어 뒤집기
"""
문자열 S가 주어졌을 때, 이 문자열에서 단어만 뒤집으려고 한다.
먼저, 문자열 S는 아래와과 같은 규칙을 지킨다.
알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '), 특수 문자('<', '>')로만 이루어져 있다.
문자열의 시작과 끝은 공백이 아니다.
'<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<'이 먼저 등장한다. 또, 두 문자의 개수는 같다.
태그는 '<'로 시작해서 '>'로 끝나는 길이가 3 이상인 부분 문자열이고, '<'와 '>' 사이에는 알파벳 소문자와 공백만 있다. 
단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고, 연속하는 두 단어는 공백 하나로 구분한다. 태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.

입력
첫째 줄에 문자열 S가 주어진다. S의 길이는 100,000 이하이다.
출력
첫째 줄에 문자열 S의 단어를 뒤집어서 출력한다.

예제 입력 1 
baekjoon online judge
예제 출력 1 
noojkeab enilno egduj
예제 입력 2 
<open>tag<close>
예제 출력 2 
<open>gat<close>
"""
class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def process(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

class WordReverser(StringProcessor):
    def __init__(self, input_string):
        super().__init__(input_string)

    def process(self):
        result = []
        temp_word = []
        inside_tag = False

        for char in self.input_string:
            if char == '<':
                # 태그 시작: 현재 단어를 뒤집고 결과에 추가
                if temp_word:
                    result.append(''.join(temp_word[::-1]))
                    temp_word = []
                inside_tag = True
                result.append(char)
            elif char == '>':
                # 태그 끝: 태그 종료를 결과에 추가
                inside_tag = False
                result.append(char)
            elif inside_tag:
                # 태그 내부: 그대로 결과에 추가
                result.append(char)
            elif char == ' ':
                # 공백: 현재 단어를 뒤집고 결과에 추가
                if temp_word:
                    result.append(''.join(temp_word[::-1]))
                    temp_word = []
                result.append(char)
            else:
                # 단어의 문자: 임시 리스트에 추가
                temp_word.append(char)

        # 마지막 단어 처리
        if temp_word:
            result.append(''.join(temp_word[::-1]))

        return ''.join(result) # return result 하면 리스트 형태로 반환돼서 

if __name__ == "__main__":
    input_string = input().strip()
    reverser = WordReverser(input_string)
    output = reverser.process()
    print(output)

# 약수의 합
"""
문제
두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다. 예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다. 
자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다. x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.
자연수 N이 주어졌을 때, g(N)을 구해보자. g(N)=g(0)+g(1)+....g(N-1)

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
출력
첫째 줄에 g(N)를 출력한다.

예제 입력 1 
1
예제 출력 1 
1
예제 입력 2 
2
예제 출력 2 
4
예제 입력 3 
10
예제 출력 3 
87
"""
class DivisorSum:
    def __init__(self, n):
        self.n = n
        self.f = [0] * (n + 1)

    def calculate_divisor_sums(self):
        # 각 숫자의 약수의 합을 계산하여 self.f 배열에 저장
        for i in range(1, self.n + 1):
            for j in range(i, self.n + 1, i):
                self.f[j] += i

class GSum(DivisorSum):
    def __init__(self, n):
        super().__init__(n)

    def calculate_g(self):
        # g(N)을 계산하기 위해 약수의 합을 먼저 계산
        self.calculate_divisor_sums() # super는 __init__처럼 자식 클래스에서 재정의 되어있지만 부모 꺼를 쓰고 싶을때

        # f 배열을 이용하여 g(N)을 계산
        g = 0
        for i in range(1, self.n + 1):
            g += self.f[i]
        return g

if __name__ == "__main__":
    # 입력
    n = int(input().strip())

    # GSum 객체 생성 및 계산
    g_sum = GSum(n)
    result = g_sum.calculate_g()

    # 출력
    print(result)

# 수 이어쓰기
"""
문제
1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.
1234567891011121314151617181920212223...
이렇게 만들어진 새로운 수는 몇 자리 수일까? 이 수의 자릿수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 100,000,000)이 주어진다.
출력
첫째 줄에 새로운 수의 자릿수를 출력한다.

예제 입력 1 
5
예제 출력 1 
5
예제 입력 2 
15
예제 출력 2 
21
"""
class DigitCalculator:
    def __init__(self, n):
        self.n = n

    def calculate(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

class TotalDigitCalculator(DigitCalculator):
    def __init__(self, n):
        super().__init__(n)

    def calculate(self):
        digits = 0
        length = 1
        start = 1

        while start <= self.n:
            end = min(self.n, start * 10 - 1)  # 현재 자리수 구간의 끝값
            digits += (end - start + 1) * length
            start *= 10
            length += 1

        return digits

if __name__ == "__main__":
    n = int(input().strip())

    # TotalDigitCalculator 객체 생성 및 계산
    calculator = TotalDigitCalculator(n)
    result = calculator.calculate()

    print(result)

# 1, 2, 3 더하기
"""
문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.
출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

예제 입력 1 
3
4
7
10
예제 출력 1 
7
44
274
"""
class SumCombinationCalculator:
    def __init__(self, max_n):
        self.max_n = max_n
        self.dp = [0] * (self.max_n + 1)
        self._precompute()

    def _precompute(self):
        # Base cases
        self.dp[0] = 1  # 0을 나타내는 방법은 한 가지(아무것도 선택하지 않음)
        if self.max_n >= 1:
            self.dp[1] = 1  # 1 = 1
        if self.max_n >= 2:
            self.dp[2] = 2  # 2 = 1+1, 2
        if self.max_n >= 3:
            self.dp[3] = 4  # 3 = 1+1+1, 1+2, 2+1, 3

        # DP를 이용해 모든 경우의 수 계산
        for i in range(4, self.max_n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2] + self.dp[i - 3]

    def get_combinations(self, n):
        return self.dp[n]

class TestCaseHandler(SumCombinationCalculator):
    def __init__(self, max_n):
        super().__init__(max_n)

    def process_test_cases(self, test_cases):
        results = []
        for n in test_cases:
            results.append(self.get_combinations(n))
        return results

if __name__ == "__main__":
    # 입력
    t = int(input().strip())
    test_cases = [int(input().strip()) for _ in range(t)]

    # 최대 n 값 찾기
    max_n = max(test_cases)

    # TestCaseHandler 객체 생성 및 처리
    handler = TestCaseHandler(max_n)
    results = handler.process_test_cases(test_cases)

    # 출력
    for result in results:
        print(result)
