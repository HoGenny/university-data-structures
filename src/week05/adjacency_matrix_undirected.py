import sys
sys.stdin = open('input.txt', 'r')

# V: 정점 개수, E: 간선 개수
V, E = map(int, input().split())

# V+1 × V+1 크기의 인접 행렬 생성 (정점 번호 1번부터 사용)
myMap = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

# 간선 정보 입력 및 인접 행렬 채우기
for _ in range(E):
    _from, _to = map(int, input().split())
    myMap[_from][_to] = 1         # 방향: _from → _to
    myMap[_to][_from] = 1         # 무방향 그래프이므로 양방향 처리

# 인접 행렬 출력
for row in myMap:
    print(row)

### 무방향 그래프의 인접 행렬 생성에 대한 기본적인 템플릿으로
### 이후 DFS, BFS, MST(최소 신장 트리) 알고리즘 구현의 기초로 활용됩니다.