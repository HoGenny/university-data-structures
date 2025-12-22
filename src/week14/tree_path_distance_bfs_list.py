import sys
sys.stdin = open("input.txt", 'r')

N, M = map(int, input().split())
g = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, w = map(int, input().split())
    g[a].append((b, w))
    g[b].append((a, w))

def BFS(start, end):
    visited = [False] * (N + 1)
    dist = [0] * (N + 1)    # 거리
    prev = [0] * (N + 1)    # 경로

    queue = [start]
    visited[start] = True

    while queue:
        curr = queue[0]
        queue = queue[1:]

        if curr == end:
            break

        for n, w in g[curr]:
            if not visited[n]:
                visited[n] = True
                prev[n] = curr
                dist[n] = dist[curr] + w
                queue.append(n)

    path = []
    node = end
    while node != 0:
        path.append(node)
        node = prev[node]
    path.reverse()

    return dist[end], path

for _ in range(M):
    u, v = map(int, input().split())
    d, p = BFS(u, v)
    print(d, end='  ')
    for i in range(len(p)):
        print(p[i], end='')
        if i != len(p) - 1:
            print('-', end='')
    print()
