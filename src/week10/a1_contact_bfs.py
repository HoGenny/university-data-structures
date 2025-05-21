import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

# BFS 함수 정의
def bfs(start, graph):
    visited = [False] * 101           # 방문 여부 기록
    depth = [0] * 101                 # 연락 받은 단계 기록
    queue = deque()
    queue.append(start)
    visited[start] = True
    max_depth = 0                     # 가장 깊은 단계 추적

    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                depth[nxt] = depth[now] + 1
                max_depth = max(max_depth, depth[nxt])
                queue.append(nxt)

    # 가장 마지막 단계에 도달한 사람 중 가장 번호 큰 사람 찾기
    result = 0
    for i in range(1, 101):
        if depth[i] == max_depth:
            result = max(result, i)
    return result

# 총 10개의 테스트케이스 처리
for tc in range(1, 11):
    length, start = map(int, input().split())
    data = list(map(int, input().split()))

    # 1~100번 사람을 정점으로 하는 인접 리스트 생성
    graph = [[] for _ in range(101)]

    # 간선 입력 (방향성 존재)
    for i in range(0, length, 2):
        _from, _to = data[i], data[i + 1]
        if _to not in graph[_from]:     # 중복 간선 방지
            graph[_from].append(_to)

    # BFS 수행 결과 출력
    answer = bfs(start, graph)
    print(f"#{tc} {answer}")

### 1238. [S/W 문제해결 기본] 10일차 - Contact