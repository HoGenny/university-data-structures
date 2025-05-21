import sys
sys.stdin = open('input.txt', 'r')

# 사용할 수 있는 3가지 능력 거리 초기화
ability = [0] * 3

# 시작 위치(샬랄라)와 목표 위치(좀비)
shalala, zombie = map(int, input().split())

# 능력치 3가지 입력
ability[0], ability[1], ability[2] = map(int, input().split())

# 각 위치에 도달하는 데 걸리는 최소 시간(또는 이동 횟수) 저장
Time = [987654321] * 1001  # 충분히 큰 수로 초기화 (무한대 역할)

# 재귀적으로 다음 위치로 이동하며 최소 시간 갱신
def getSome(here):
    if here > zombie:
        return  # 목표를 초과하면 더 이상 진행하지 않음
    for i in range(3):
        next = here + ability[i]
        if next <= 1000 and Time[next] > Time[here] + 1:
            Time[next] = Time[here] + 1
            getSome(next)

# 시작 위치의 시간은 0
Time[shalala] = 0

# 시작과 목표가 같으면 바로 종료
if shalala == zombie:
    print(0)
else:
    getSome(shalala)  # 탐색 시작

# 결과 출력
if Time[zombie] != 987654321:
    print(Time[zombie])
else:
    print(-1)  # 도달 불가능한 경우
