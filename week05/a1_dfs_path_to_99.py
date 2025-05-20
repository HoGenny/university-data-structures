import sys
sys.stdin = open('input.txt', 'r')

# DFS 함수 정의: 현재 위치 here에서 99로 갈 수 있는 경로 찾기
def DFS(here):
    Visited[here] = True

    # 목적지(99번 노드)에 도착하면 경로 수 증가
    if here == 99:
        global ans
        ans += 1
        return

    # 인접한 노드들을 방문
    for next in range(100):
        if RoadMap[here][next] and not Visited[next]:
            DFS(next)

# 총 10개의 테스트케이스 실행
T = 10
for _ in range(T):
    tc, E = map(int, input().split())                # 테스트케이스 번호, 간선 수
    Data = list(map(int, input().split()))           # 간선 정보

    RoadMap = [[0] * 100 for _ in range(100)]        # 100x100 인접 행렬
    ans = 0                                           # 도착 경로 수
    Visited = [False] * 100                           # 방문 여부

    # 간선 정보 반영
    for i in range(E):
        _from = Data[2 * i]
        _to = Data[2 * i + 1]
        RoadMap[_from][_to] = 1                       # 방향성 그래프 (단방향)

    # DFS 탐색 시작 (0번 노드에서 시작)
    DFS(0)

    # 결과 출력
    print(f"#{tc} {ans}")

### 1219. [S/W 문제해결 기본] 4일차 - 길찾기