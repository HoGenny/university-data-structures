import sys
sys.stdin = open('input.txt', 'r')

# 상하좌우 방향 벡터
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

# DFS로 미로 탐색
def getSome(y, x):
    global found

    # 도착지점(3)을 만나면 탐색 종료
    if myMap[y][x] == 3:
        found = True
        return

    # 현재 위치 방문 표시
    myMap[y][x] = -1

    # 4방향 탐색
    for dir in range(4):
        newY = y + dy[dir]
        newX = x + dx[dir]

        # 벽이 아니고, 방문하지 않은 경로라면 재귀 호출
        if myMap[newY][newX] != 1 and myMap[newY][newX] != -1:
            getSome(newY, newX)

# 총 10개의 테스트케이스 처리
for tc in range(1, 11):
    input()  # 테스트케이스 번호 (사용 X)
    
    # 16x16 미로 입력 (한 줄씩 정수 리스트로 변환)
    myMap = [list(map(int, input())) for _ in range(16)]

    found = False

    # 출발점은 항상 (1, 1) 위치
    getSome(1, 1)

    # 결과 출력
    if found:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")

### 1226. [S/W 문제해결 기본] 7일차 - 미로1 