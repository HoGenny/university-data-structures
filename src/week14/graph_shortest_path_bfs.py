import sys
sys.stdin = open('input.txt', 'r')

def BFS(S, G):
    queue = [S]
    visited[S] = 1
    while queue:
        v = queue.pop(0)
        for i in g[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                queue.append(i)
            if i == G:
                return visited[i] - 1
    return 0

V, E = map(int, input().split())
g = [[] for _ in range(V+1)]
visited = [0] * (V + 1)

for _ in range(E):
    i, j = map(int, input().split())
    g[i].append(j)
    g[j].append(i)

S, G = map(int, input().split())
answer = BFS(S, G)
print(answer)