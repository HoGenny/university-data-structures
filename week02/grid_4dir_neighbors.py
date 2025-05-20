# 5x5 정수형 2차원 리스트 생성
data = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

# 상, 하, 좌, 우를 표현하는 방향 벡터
dy = [-1, 1, 0, 0]  # y방향: 위, 아래
dx = [0, 0, -1, 1]  # x방향: 왼쪽, 오른쪽

# 특정 값 11의 위치를 찾기 위한 좌표 변수 초기화
whereY = -1
whereX = -1

# 11이 있는 위치 탐색
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 11:
            whereY = y
            whereX = x

# 상하좌우 인접 좌표 탐색 및 출력
for dir in range(4):
    newY = whereY + dy[dir]
    newX = whereX + dx[dir]

    # 인덱스 범위 내에 있을 경우 출력
    if 0 <= newY < 5 and 0 <= newX < 5:
        print(data[newY][newX])

### 이 코드는 2차원 배열에서 특정 값의 위치를 찾아 상하좌우 인접값을 출력하는 방식입니다.
### 격자 탐색 문제의 기초이며, BFS/DFS 등에서도 많이 활용됩니다.