import sys
sys.stdin = open('input.txt', 'r')

# 3가지 이동 능력 초기화
ability = [0] * 3

# 시작 위치(샬랄라), 목표 위치(좀비) 입력
shalala, zombie = map(int, input().split())

# 각 능력치 입력 (샬랄라가 한 번에 이동 가능한 거리들)
ability[0], ability[1], ability[2] = map(int, input().split())

# 위치별 최소 이동 횟수 저장용 리스트 (987654321은 무한을 의미)
Time = [987654321] * 1001

# 재귀적으로 이동 가능 경로를 탐색하며 최소 이동 횟수 저장
def getSome(here):
    # 목표보다 멀리 간 경우는 탐색하지 않음
    if here > zombie:
        return

    for i in range(3):
        next = here + ability[i]

        # 범위 확인 및 더 빠른 경로일 때만 갱신
        if next <= 1000 and Time[next] > Time[here] + 1:
            Time[next] = Time[here] + 1
            getSome(next)

# 시작 지점의 이동 횟수는 0으로 초기화
Time[shalala] = 0

# 시작 지점과 목표가 같다면 바로 출력
if shalala == zombie:
    print(0)
else:
    getSome(shalala)

# 결과 출력: 도달 가능하면 최소 시간, 아니면 -1
if Time[zombie] != 987654321:
    print(Time[zombie])
else:
    print(-1)