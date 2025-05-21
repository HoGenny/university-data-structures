import sys
sys.stdin = open('input.txt', 'r')

# DFS 함수 정의 (재귀 방식)
def DFS(V):
    print(f'{V}', end=' ')        # 현재 노드 출력
    visited[V] = True             # 방문 처리

    # 정점 번호가 작은 순서대로 탐색
    for next in range(1, N + 1):
        if myMap[V][next] == 1 and not visited[next]:
            DFS(next)

# 정점 수 N, 간선 수 M, 시작 정점 V 입력
N, M, V = map(int, input().split())

# 인접 행렬 초기화 (1-based index)
myMap = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 방문 여부 리스트 초기화
visited = [False] * (N + 1)

# 간선 정보 입력
for _ in range(M):
    start, stop = map(int, input().split())
    myMap[start][stop] = 1
    myMap[stop][start] = 1  # 무방향 그래프

# DFS 실행
DFS(V)