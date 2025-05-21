import sys
sys.stdin = open('input.txt', 'r')

# 지도 크기 N (N x N)
N = int(input())

# 2차원 지도 입력 (문자 → 정수 변환)
myMap = [[int(c) for c in input().strip()] for _ in range(N)]

# 단지 수
count = 0

# 단지별 집 개수를 저장할 리스트 (최대 100개 가정)
house = [0] * 100

# 상하좌우 이동 벡터
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

# DFS를 이용한 단지 탐색
def DFS(y, x):
    house[count] += 1  # 현재 단지 집 수 증가
    myMap[y][x] = -1   # 방문 표시

    for dir in range(4):
        newY = y + dy[dir]
        newX = x + dx[dir]

        # 유효 범위 안에서, 연결된 집(1)이면 계속 탐색
        if 0 <= newY < N and 0 <= newX < N and myMap[newY][newX] == 1:
            DFS(newY, newX)

# 전체 지도를 순회하면서 DFS 실행
for i in range(N):
    for j in range(N):
        if myMap[i][j] == 1:
            DFS(i, j)
            count += 1  # 단지 수 증가

# 정렬하여 출력
sorted_house = sorted(house[:count])
print(count)
for h in sorted_house:
    print(h)

### 백준 2667. 단지번호붙이기