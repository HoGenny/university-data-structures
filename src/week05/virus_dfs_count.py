import sys
sys.stdin = open('input.txt', 'r')

# 컴퓨터 수 (정점 수)
V = int(input())

# 연결 수 (간선 수)
E = int(input())

# 인접 리스트 초기화 (1번부터 V번까지)
myMap = [[] for _ in range(V + 1)]

# 양방향 연결 정보 저장
for _ in range(E):
    _from, _to = map(int, input().split())
    myMap[_from].append(_to)
    myMap[_to].append(_from)

# 방문 여부를 저장할 리스트
visited = [False] * (V + 1)

# 감염된 컴퓨터 수를 저장할 변수
ans = 0

# 감염될 컴퓨터를 담는 스택 (DFS)
infected = [1]  # 1번 컴퓨터가 최초 감염

# DFS 탐색
while True:
    if len(infected) == 0:
        break
    zombie = infected.pop()  # 감염된 컴퓨터 하나 꺼냄
    if visited[zombie] == False:
        visited[zombie] = True  # 방문 처리
        ans += 1                # 감염된 컴퓨터 수 증가
        for next in myMap[zombie]:
            infected.append(next)  # 연결된 컴퓨터를 스택에 추가

# 1번 컴퓨터 자신 제외하고 출력
print(ans - 1)

### DFS 탐색 기반 바이러스 문제로, 백준 2606번 '바이러스' 문제와 동일한 유형입니다.