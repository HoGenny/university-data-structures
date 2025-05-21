import sys
sys.stdin = open('input.txt', 'r')

# BFS 함수 정의
def BFS():
    while Queue:
        here = Queue.pop(0)          # 현재 노드 꺼냄
        visited[here] = True         # 방문 처리
        print(here, end=' ')         # 현재 노드 출력

        # 인접 노드 탐색
        for next in range(1, howMany + 1):
            if not visited[next] and myMap[here][next]:
                parent[next] = here                      # 부모 노드 저장
                distance[next] = distance[here] + 1      # 거리 저장
                visited[next] = True                     # 방문 표시
                Queue.append(next)                       # 큐에 추가

# 정점 수와 간선 수 입력
howMany, E = map(int, input().split())

# 인접 행렬 초기화
myMap = [[0 for _ in range(howMany + 1)] for _ in range(howMany + 1)]

# 방문 여부, 부모 정보, 거리 정보 초기화
visited = [False] * (howMany + 1)
parent = [0] * (howMany + 1)
distance = [-1] * (howMany + 1)

# 간선 정보 입력
for _ in range(E):
    start, stop = map(int, input().split())
    myMap[start][stop] = 1
    myMap[stop][start] = 1  # 무방향 그래프

# 시작점 설정
Queue = [1]
parent[1] = -1       # 시작점은 부모 없음
distance[1] = 0      # 시작점 거리 0

# BFS 실행
BFS()

# 줄바꿈 후 결과 출력
print()
print(parent)    # 각 노드의 부모 정보
print(distance)  # 각 노드까지의 거리 정보