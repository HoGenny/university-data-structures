# 📌 9주차 - 재귀 알고리즘 & 그래프 탐색(DFS, BFS)

이번 주는 **재귀 함수(Recursion)** 개념을 중심으로 **DFS/BFS 탐색**, **요세푸스 문제**, **하노이의 탑** 등 다양한 고전 알고리즘을 실습하였습니다.

---

## 📚 학습 내용

### ✅ 재귀 함수 (Recursion)

- 함수가 자기 자신을 호출하여 문제를 해결
- 하노이의 탑, 요세푸스 문제 등 반복적 구조를 간결하게 표현
- 재귀 깊이와 탈출 조건 설정이 중요

### ✅ 그래프 탐색

| 탐색 방식 | 설명 | 활용 |
|-----------|------|------|
| DFS (Depth-First Search) | 깊이 우선, 스택 기반 | 백트래킹, 경로 탐색 |
| BFS (Breadth-First Search) | 너비 우선, 큐 기반 | 최단 거리, 감염 확산 시뮬레이션 등 |

---

## 🧪 실습 파일 설명

### ▶ `hanoi_recursive.py`
- 하노이의 탑 문제를 재귀로 해결
- 최소 이동 횟수: 2ⁿ - 1

### ▶ `josephus_deque.py`
- `collections.deque`를 이용한 요세푸스 문제 구현

### ▶ `josephus_simulation.py`
- 리스트 기반 요세푸스 시뮬레이션 (시간 복잡도 증가)

### ▶ `dfs_adjacency_matrix.py`
- 인접 행렬을 이용한 깊이 우선 탐색(DFS) 구현

### ▶ `bfs_parent_distance.py`
- BFS 탐색으로 각 노드의 부모와 거리 기록
- 트리 구조나 최단 거리 문제에 활용 가능

### ▶ `reach_zombie_recursive.py`
- 좀비 감염 시나리오에서 **재귀적** 전파 구현
- DFS 방식으로 감염 여부 판별

---

## 💡 정리 포인트

- 재귀는 직관적이지만 **스택 오버플로우** 주의 필요
- DFS/BFS는 **그래프 표현 방식(인접 행렬, 인접 리스트)**에 따라 성능 차이 발생
- 요세푸스 문제는 자료구조 선택에 따라 시간 차이 큼

---

📂 실습 파일:  
- `hanoi_recursive.py`, `josephus_deque.py`, `josephus_simulation.py`  
- `dfs_adjacency_matrix.py`, `bfs_parent_distance.py`, `reach_zombie_recursive.py`

✍️ 과제:
- 하노이의 탑 단계별 이동 출력 구현
- DFS/BFS를 비교 분석하고 그래프마다 적용해보기
- 요세푸스 문제를 큐 기반으로 일반화

---

**_다음 주는 정렬 알고리즘과 BFS 실전 문제로 이어집니다._**