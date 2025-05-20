# 절댓값을 반환하는 함수 정의 (내장 abs 사용 안 함)
def myAbs(a):
    return a if a > 0 else -a

# 좌표가 유효한 범위(5x5) 안에 있는지 검사하는 함수
def isSafe(y, x):
    return 0 <= y < 5 and 0 <= x < 5

# 5x5 2차원 배열 정의
data = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

# 상하좌우 방향 벡터
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 결과값 누적용 변수 초기화
sum = 0

# 모든 좌표 순회
for y in range(5):
    for x in range(5):
        # 현재 좌표에서 상하좌우 인접한 좌표 검사
        for dir in range(4):
            newY = y + dy[dir]
            newX = x + dx[dir]
            if isSafe(newY, newX):
                # 인접한 값과의 차이 절댓값을 누적
                sum += myAbs(data[y][x] - data[newY][newX])

# 최종 합 출력
print(sum)

### 이 코드는 2차원 배열에서 각 원소와 상하좌우 인접한 값들 간의 절댓값 차이의 합을 구하는 문제입니다.