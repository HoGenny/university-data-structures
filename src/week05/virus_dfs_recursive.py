import sys
sys.stdin = open('input.txt', 'r')

# 컴퓨터 수 (정점 수)
V = int(input())

# 연결 수 (간선 수)
E = int(input())

# 인접 리스트 초기화 (1번부터 V번까지)
myMap = [[] for _ in range(V + 1)]

# 양방향 연결 정보 저장
for _ in range(E):
    _from, _to = map(int, input().split())
    myMap[_from].append(_to)
    myMap[_to].append(_from)

# 방문 여부 배열
visited = [False] * (V + 1)

# 감염된 컴퓨터 수를 저장할 변수
ans = 0

# DFS 재귀 함수 정의
def DFS(zombie):
    global ans
    ans += 1                 # 감염된 컴퓨터 수 증가
    visited[zombie] = True   # 방문 처리

    # 연결된 컴퓨터 중 아직 방문하지 않은 곳으로 재귀 탐색
    for next in myMap[zombie]:
        if not visited[next]:
            DFS(next)

# 1번 컴퓨터에서 시작
DFS(1)

# 자신(1번 컴퓨터) 제외하고 출력
print(ans - 1)

### 재귀 DFS를 통해 바이러스가 감염시킬 수 있는 컴퓨터의 수를 계산합니다.
### 감염 시작점은 1번 컴퓨터이며, 감염 대상 수는 자기자신을 제외한 수 (ans - 1)입니다.
### 백준 2606번 '바이러스' 문제와 동일한 유형입니다.