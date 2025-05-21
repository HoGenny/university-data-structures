import sys
sys.stdin = open('input.txt', 'r')

# BFS 함수 정의
def BFS():
    while queue:
        here = queue.pop(0)       # 큐에서 현재 노드 꺼내기
        visited[here] = True      # 방문 처리
        print(here)               # 현재 노드 출력

        # 인접 노드 순회
        for next in range(1, howmany + 1):
            if myMap[here][next] and not visited[next]:
                visited[next] = True
                queue.append(next)

# 정점 수와 간선 수 입력
howmany, E = map(int, input().split())

# 인접 행렬 초기화 (1번 노드부터 시작)
myMap = [[0 for _ in range(howmany + 1)] for _ in range(howmany + 1)]

# 방문 여부 배열
visited = [0] * (howmany + 1)

# 간선 정보 입력 (무방향 그래프)
for _ in range(E):
    start, stop = map(int, input().split())
    myMap[start][stop] = 1
    myMap[stop][start] = 1

# BFS 시작점 설정
queue = [1]
BFS()

### 너비 우선 탐색의 기본적인 예제입니다.