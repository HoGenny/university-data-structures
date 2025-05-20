import sys
sys.stdin = open('input.txt', 'r')

# 깊이 우선 탐색 (재귀)
def DFS(here):
    print(f'{here}', end=' ')
    visited[here] = True
    for next in range(1, N + 1):
        if myMap[here][next] == 1 and not visited[next]:
            DFS(next)

# 너비 우선 탐색 (큐)
def BFS():
    while queue:
        here = queue.pop(0)
        visited[here] = True
        print(f'{here}', end=' ')
        for next in range(1, N + 1):
            if myMap[here][next] == 1 and not visited[next]:
                visited[next] = True
                queue.append(next)

# 입력: 정점 수 N, 간선 수 M, 시작 정점 V
N, M, V = map(int, input().split())

# 인접 행렬 초기화
myMap = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 방문 배열 초기화
visited = [0] * (N + 1)

# 간선 입력 (무방향 그래프)
for _ in range(M):
    start, stop = map(int, input().split())
    myMap[start][stop] = 1
    myMap[stop][start] = 1

# DFS 수행
DFS(V)
print()

# BFS 준비
visited = [0] * (N + 1)
queue = [V]

# BFS 수행
BFS()

### 백준 1260. DFS와 BFS