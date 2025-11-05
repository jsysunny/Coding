N = int(input())
seats = input()
seats=list(seats)
# Please write your code here.

max_min_dist = 0

for i in range(N):
    if seats[i] == '0':
        # 이 자리에 사람을 앉혀본다
        seats[i] = '1'
        people = [j for j in range(N) if seats[j] == '1']
        
        # 인접한 사람들 사이의 거리 최소값 계산
        min_dist = min(people[i+1] - people[i] for i in range(len(people) - 1))
        
        # 최대 거리 중 최소를 업데이트
        max_min_dist = max(max_min_dist, min_dist)
        
        # 원래대로 되돌림
        seats[i] = '0'

print(max_min_dist)

        

        
        
