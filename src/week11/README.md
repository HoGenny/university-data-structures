# 📌 11주차 - 정렬 알고리즘 심화 및 빠른 거듭제곱

이번 주는 다양한 정렬 알고리즘과 함께, 지수 계산을 빠르게 처리하는 **빠른 거듭제곱(Fast Exponentiation)** 기법을 학습했습니다.

---

## 📚 학습 내용

### ✅ 주요 정렬 알고리즘

| 알고리즘 | 시간 복잡도 | 특징 |
|----------|-------------|------|
| 카운팅 정렬 (Counting Sort) | O(n + k) | 정수 배열, 범위 작을 때 효율적 |
| 퀵 정렬 (Quick Sort) | 평균: O(n log n), 최악: O(n²) | 분할 정복, 피벗 기준 정렬 |
| 병합 정렬 (Merge Sort) | O(n log n) | 안정 정렬, 메모리 추가 필요 |
| 셸 정렬 (Shell Sort) | O(n log² n) 또는 그 이상 | 삽입 정렬 기반, 간격 줄여가며 정렬 |

---

### ✅ 지수 계산 최적화

#### 📌 빠른 거듭제곱 (Fast Exponentiation)
- 반복문 또는 분할정복을 이용해 거듭제곱을 빠르게 계산
- 시간 복잡도: O(log n)

---

## 🧪 실습 파일 설명

### ▶ `a1_quick_sort.py`, `quick_sort_partitioned.py`, `quick_sort_hoare.py`
- 다양한 방식의 퀵 정렬 구현
- 피벗 선택 방식과 파티셔닝 로직에 따라 성능 차이 비교

### ▶ `a2_counting_sort.py`
- 정수형 데이터에 최적화된 카운팅 정렬 구현
- 중복값과 최대값 고려

### ▶ `a3_merge_sort.py`, `merge_sort_recursive.py`, `merge_two_sorted_lists.py`
- 병합 정렬 전체 구현 및 재귀 방식
- 두 정렬 리스트를 병합하는 유틸리티 함수 포함

### ▶ `shell_sort.py`
- 간격(gap)을 조정하며 수행하는 삽입 정렬 확장판
- 효율적인 부분 정렬

### ▶ `fast_exponentiation.py`
- 지수 계산을 O(log n) 시간에 수행
- 반복 및 재귀 방식 모두 활용 가능

---

## 💡 정리 포인트

- 정렬 알고리즘은 입력 데이터의 **특성과 크기**에 따라 선택해야 한다.
- **퀵 정렬**은 평균적으로 빠르지만, **최악의 경우** O(n²)일 수 있으므로 주의가 필요하다.
- **병합 정렬**은 항상 O(n log n) 성능을 보장하지만, **공간 복잡도**가 높다.
- **셸 정렬**은 이론적으로 불완전하지만 실제 데이터에서는 상당히 빠르다.
- **빠른 거듭제곱**은 알고리즘 문제 풀이 시 필수 테크닉이다.

---

📂 실습 파일:  
- `a1_quick_sort.py`, `quick_sort_partitioned.py`, `quick_sort_hoare.py`  
- `a2_counting_sort.py`  
- `a3_merge_sort.py`, `merge_sort_recursive.py`, `merge_two_sorted_lists.py`  
- `shell_sort.py`, `fast_exponentiation.py`

✍️ 과제:
- 다양한 데이터 크기와 분포에서 정렬 속도 비교 실험
- 반복문 기반 거듭제곱과 빠른 거듭제곱 비교

---

**_다음 주는 문자열 알고리즘으로 이어집니다!_**