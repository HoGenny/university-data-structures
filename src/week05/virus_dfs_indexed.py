import sys
sys.stdin = open('input.txt', 'r')

# 정점 수, 간선 수 입력
V = int(input())
E = int(input())

# 인접 리스트 초기화
myMap = [[] for _ in range(V + 1)]

# 간선 입력 (양방향)
for _ in range(E):
    _from, _to = map(int, input().split())
    myMap[_from].append(_to)
    myMap[_to].append(_from)

# 방문 여부 기록
visited = [False] * (V + 1)
ans = 0

# DFS 정의
def DFS(here):
    global ans
    print(here)             # 방문한 노드 출력
    visited[here] = True
    ans += 1

    # 현재 정점에서 인접한 정점들 순회
    for next in myMap[here]:
        if not visited[next]:
            DFS(next)

# 1번 정점에서 시작
DFS(1)

# 출력: 1번 제외한 감염 수
print(ans - 1)