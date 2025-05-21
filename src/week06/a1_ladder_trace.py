import sys
sys.stdin = open('input.txt', 'r')

# 방향 벡터: 좌, 우, 상 (왼쪽, 오른쪽, 위쪽으로만 이동 가능)
dy = [0, 0, -1]
dx = [-1, 1, 0]

# 이동 가능한 좌표인지 확인
def isPossible(y, x):
    return 0 <= y < 100 and 0 <= x < 100 and myMap[y][x] == 1

# 사다리를 타고 위쪽으로 추적하는 재귀 함수
def getSome(y, x):
    myMap[y][x] = -1  # 방문 처리 (중복 방지)

    # 맨 위에 도달했으면 정답 출력
    if y == 0:
        print("#%d" % tc, x)
        return

    # 좌 → 우 → 상 순서로 우선 이동 가능 여부 확인
    for dir in range(3):
        newY = y + dy[dir]
        newX = x + dx[dir]
        if isPossible(newY, newX):
            getSome(newY, newX)
            return  # 경로 하나만 찾으면 되므로 종료

# 10개의 테스트 케이스 수행
for tc in range(1, 11):
    input()  # 테스트 케이스 번호 (사용 안 함)

    # 100x100 사다리 맵 입력 받기
    myMap = [list(map(int, input().split())) for _ in range(100)]

    # 도착 지점(2) 위치 찾기 (가장 아래 줄에서)
    for x in range(100):
        if myMap[99][x] == 2:
            startX = x

    # 도착 지점에서 위로 추적 시작
    getSome(99, startX)

### 1210. [S/W 문제해결 기본] 2일차 - Ladder1