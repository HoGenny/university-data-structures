import sys
sys.stdin = open('in.txt', 'r')

# 시작점(샬랄라)와 목표점(좀비) 위치 입력
shalala, zombie = map(int, input().split())

# 3가지 이동 능력 입력
ability = list(map(int, input().split()))

# BFS용 큐와 거리 저장 배열 초기화
queue = []
Time = [987654321] * 1000  # 충분히 큰 값으로 초기화 (== 무한)

# BFS 함수 정의
def BFS():
    while queue:
        here = queue.pop(0)  # 현재 위치 꺼냄
        for i in range(3):
            next = here + ability[i]
            if next >= len(Time):  # 범위를 초과하면 무시
                continue
            if Time[next] > Time[here] + 1:
                Time[next] = Time[here] + 1
                queue.append(next)

# 시작 위치 초기화
Time[shalala] = 0
queue.append(shalala)

# BFS 수행
BFS()

# 결과 출력
if Time[zombie] != 987654321:
    print(Time[zombie])  # 최소 이동 횟수 출력
else:
    print(-1)  # 도달 불가능할 경우