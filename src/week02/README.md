# 📌 02주차 - 카운팅 정렬 & 2차원 리스트 기초

카운팅 정렬의 핵심 로직과 빈도수 배열 구축을 실습하고, 2차원 격자/리스트 순회, 좌표 탐색, 기본적인 입력 처리 패턴을 다뤘습니다.

---

## 🗂️ 파일 목록

| 파일명 | 설명 |
|--------|------|
| `counting_sort.py` | 빈도수 → 누적합 → 재배치까지 포함한 완전한 카운팅 정렬 구현 |
| `counting_sort_count.py` | 카운트 배열을 이용해 각 숫자 등장 횟수만 집계하는 버전 (for 인덱스) |
| `counting_sort_count_foreach.py` | 위와 동일한 빈도수 집계를 for-each 스타일로 구현 |
| `a1_find_most_frequent_score.py` | SWEA 1204 최빈수 구하기: 0~100 점수의 최빈값 계산 |
| `a2_kill_fly.py` | SWEA 12712 파리퇴치3: 십자/대각선 범위 합의 최대값 찾기 |
| `grid_4dir_neighbors.py` | 2차원 격자에서 특정 값(11)의 상하좌우 인접값 출력 |
| `sum_abs_diff_neighbors.py` | 격자 내 모든 칸의 상하좌우 차이 절댓값 합산 |
| `print_2d_jagged.py` | 가변 길이(비정형) 2차원 리스트 순회 예제 |
| `print_grid_5x5.py` | 중첩 반복문으로 1~25를 5x5 격자 형태로 출력 |
| `itoa.py` | 정수를 문자열 리스트로 직접 분해해 저장하는 `itoa` 구현 예제 |
| `menu_dict_input.py` | 입력으로 메뉴/가격을 받아 딕셔너리에 저장하고 조회하는 기본 패턴 |

---

## 📌 학습 포인트

- 카운팅 정렬 흐름: 빈도수 계산 → 누적합 → 역순 재배치
- 2차원 격자에서 방향 벡터(`dy`, `dx`)로 인접 좌표 탐색
- 가변 길이 2차원 리스트 순회 시 `len(row)`를 활용한 범위 제어
- 입력을 파일로 리다이렉트해 테스트케이스를 반복 처리하는 SWEA 스타일 입출력
- 딕셔너리 기본 사용법(삽입, 조회)과 단순 반복 입력 처리

---

## 💡 실행 예시

```bash
# 카운팅 정렬
python counting_sort.py

# SWEA 1204/12712 스타일 문제 (input.txt를 동일 디렉터리나 상위 루트에 준비)
python a1_find_most_frequent_score.py < input.txt
python a2_kill_fly.py < input.txt
```

`input.txt`는 실행 위치 기준으로 열리므로, 필요한 케이스를 현재 폴더나 프로젝트 루트에 맞게 배치한 뒤 실행하세요.
