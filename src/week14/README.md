# 📌 14주차 - 연결 리스트 심화 & BFS 탐색 응용

단순 연결 리스트의 기본 순회부터 삽입/삭제, 원형 리스트를 활용한 요세푸스 문제까지 실습했습니다.  
또한 그래프/트리에서 BFS로 최단 거리와 경로를 구하는 예제를 정리했습니다.

---

## 🗂️ 파일 목록

| 파일명 | 설명 |
|--------|------|
| `singly_linked_list_traversal.py` | 노드 생성 후 단순 연결 리스트를 순회하며 데이터 출력 |
| `singly_linked_list_insert_delete.py` | 특정 위치 삽입과 데이터 값 기준 삭제를 구현한 단순 연결 리스트 |
| `josephus_circular_linked_list.py` | 원형 연결 리스트로 요세푸스 문제를 해결하여 마지막 두 사람을 출력 |
| `stack_with_linked_list.py` | 연결 리스트를 이용한 스택 `push/pop/top` 구현 |
| `graph_shortest_path_bfs.py` | 무가중치 그래프에서 시작–도착 정점 사이의 최단 간선 수를 BFS로 계산 |
| `graph_shortest_path_bfs_multi.py` | 여러 테스트 케이스에 대해 최단 간선 수를 반복 계산하는 BFS 버전 |
| `tree_path_distance_bfs_list.py` | 가중치 트리에서 BFS로 두 노드 사이 거리 합과 경로를 복원 (리스트 큐) |
| `tree_path_distance_bfs_deque.py` | `deque`를 사용해 위 트리 경로 복원 로직을 큐 효율을 높여 구현 |
| `input.txt` | 그래프 예제 입력 (무가중치 최단 거리 확인용) |

---

## 📌 학습 포인트

- 단순/원형 연결 리스트 노드 연결 방식과 포인터 이동 로직
- 연결 리스트 기반 삽입·삭제, 스택 구현 시의 헤드/탑 관리 방법
- BFS로 무가중치 그래프의 최단 간선 수를 계산하는 패턴 (`visited`에 거리 누적)
- 트리에서 부모 추적 배열을 활용해 최단 경로를 역추적하고, 가중치 합을 계산하는 방법

---

## 💡 실행 예시

```bash
# 그래프 최단 거리 (무가중치)
python graph_shortest_path_bfs.py < input.txt

# 트리 경로 및 거리 (가중치) - 입력 파일 교체 가능
python tree_path_distance_bfs_list.py < input.txt
```

각 스크립트는 표준 입력을 사용하므로, 필요한 경우 `input.txt` 내용을 문제에 맞게 수정한 뒤 실행하세요.
