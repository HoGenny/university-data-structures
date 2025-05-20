import sys
sys.stdin = open('input.txt', 'r')

# 좌표가 격자 내에 있는지 확인하는 함수
def isSafe(y, x, N):
    return 0 <= x < N and 0 <= y < N

# 테스트 케이스 반복
for tc in range(int(input())):
    N, M = map(int, input().split())  # N: 격자 크기, M: 확산 범위

    # 격자 입력 (N×N 크기)
    myMap = [list(map(int, input().split())) for _ in range(N)]
    result = 0  # 최대 합 저장 변수

    # 십자 방향 (상, 우, 하, 좌)
    dy1 = [-1, 0, 1, 0]
    dx1 = [0, 1, 0, -1]

    for y in range(N):
        for x in range(N):
            sum = myMap[y][x]  # 시작점 포함
            for dir in range(4):  # 4방향으로
                for size in range(1, M):  # M-1칸까지 확장
                    newY, newX = y + dy1[dir] * size, x + dx1[dir] * size
                    if isSafe(newY, newX, N):
                        sum += myMap[newY][newX]
            if sum > result:
                result = sum  # 최대값 갱신

    # 대각선 방향 (↙, ↘, ↖, ↗)
    dy2 = [1, 1, -1, -1]
    dx2 = [-1, 1, -1, 1]

    for y in range(N):
        for x in range(N):
            sum = myMap[y][x]  # 시작점 포함
            for dir in range(4):  # 4방향 대각선
                for size in range(1, M):
                    newY, newX = y + dy2[dir] * size, x + dx2[dir] * size
                    if isSafe(newY, newX, N):
                        sum += myMap[newY][newX]
            if sum > result:
                result = sum  # 최대값 갱신

    # 결과 출력 (테스트케이스 번호 포함)
    print(f'#{tc+1} {result}')

### SWEA 12712. 파리퇴치3