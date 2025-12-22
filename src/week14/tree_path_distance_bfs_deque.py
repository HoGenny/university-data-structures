import sys
sys.stdin = open("input.txt", 'r')

from collections import deque, defaultdict

# 입력
N, M = map(int, input().split())
graph = defaultdict(list)

# 트리 구성
for _ in range(N - 1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

# BFS: 경로 + 거리
def bfs(start, end):
    visited = [False] * (N + 1)
    prev = [0] * (N + 1)  # 경로 추적용
    dist = [0] * (N + 1)
    
    queue = deque([start])
    visited[start] = True
    
    while queue:
        curr = queue.popleft()
        if curr == end:
            break
        for neighbor, weight in graph[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                prev[neighbor] = curr
                dist[neighbor] = dist[curr] + weight
                queue.append(neighbor)
    
    # 경로 복원
    path = []
    node = end
    while node != 0:
        path.append(node)
        node = prev[node]
    path.reverse()
    
    return dist[end], path

# 쿼리 처리
for _ in range(M):
    u, v = map(int, input().split())
    d, p = bfs(u, v)
    print(f"{d}  {'-'.join(map(str, p))}")
