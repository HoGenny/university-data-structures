# 📌 7주차 - 그래프 탐색 (DFS/BFS) & 큐 기본 개념

이번 주는 **그래프 탐색 알고리즘(DFS, BFS)** 과 **큐(Queue)** 자료구조의 기본 개념 및 활용법을 학습했습니다.  
또한, 간단한 **미로 탈출 문제**, **격자형 연결 요소 탐색**, **요세푸스 문제 응용** 등을 실습했습니다.

---

## 📚 학습 내용

### ✅ DFS / BFS

| 알고리즘 | 특징 | 주로 사용되는 상황 |
|----------|------|--------------------|
| DFS (깊이 우선 탐색) | Stack 기반, 재귀로 구현 가능 | 경로 찾기, 백트래킹 |
| BFS (너비 우선 탐색) | Queue 기반 | 최단 거리, 단계별 탐색 |

### ✅ 큐 (Queue)
- FIFO(First In First Out) 구조
- `enqueue` (삽입), `dequeue` (삭제) 연산
- BFS 구현에서 핵심 자료구조

---

## 🧪 실습 파일 설명

### ▶ `a1_maze_solver_dfs.py`
- DFS를 활용한 미로 탈출 문제
- 벽(0)과 통로(1)로 구성된 맵에서 출구 탐색

### ▶ `a2_dfs_bfs_traversal.py`
- DFS와 BFS의 기초 구현 및 출력 순서 비교
- 인접 리스트 기반

### ▶ `a3_dfs_connected_components_grid.py`
- DFS를 통해 2차원 격자의 연결 요소(connected components) 수 세기
- 전형적인 DFS 연습 문제

### ▶ `bfs_graph_traversal.py`
- 큐를 이용한 BFS 탐색 구현
- 노드 방문 순서를 정확히 추적

---

### ▶ `queue_basic.py`
- 큐의 기본 개념 설명 및 사용 예시
- 리스트와 `collections.deque` 비교

### ▶ `josephus_modified.py`
- 요세푸스 문제의 큐 기반 응용
- 순서대로 제거되며 마지막 남는 번호 출력

---

## 💡 정리 포인트

- DFS는 재귀 또는 스택으로 구현 가능하며, 깊은 경로를 먼저 탐색
- BFS는 큐를 사용하여 너비 방향으로 순차적 탐색
- 큐는 BFS뿐 아니라 시뮬레이션, 대기열 모델링 등에서 매우 자주 쓰임
- 연결 요소 탐색은 DFS 연습에 좋은 문제 유형

---

📂 실습 파일:  
- `a1_maze_solver_dfs.py`, `a2_dfs_bfs_traversal.py`, `a3_dfs_connected_components_grid.py`  
- `bfs_graph_traversal.py`, `queue_basic.py`, `josephus_modified.py`

✍️ 과제:
- 미로 문제에서 출구까지의 경로 출력 구현
- DFS와 BFS 방문 순서 비교 예제 추가
- 연결 요소 수 세는 DFS → BFS 버전으로도 구현해 보기

---

**_8주차는 중간고사 주간으로 별도 수업은 없습니다._**