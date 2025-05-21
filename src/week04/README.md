# 📌 4주차 - 스택 응용, 재귀 함수, 정렬 기초

이번 주는 **스택(Stack)** 구조의 대표적인 활용인 **괄호 검사**,  
기초적인 **재귀 함수(Recursion)** 예제들, 그리고 **선택 정렬(Selection Sort)** 구현을 실습했습니다.

---

## 📚 학습 내용

### ✅ 스택 활용: 괄호 검사

| 구현 방식 | 설명 |
|-----------|------|
| `bracket_matching_stack.py` | 전형적인 스택 활용 괄호 짝 검사 |
| `bracket_matching_dict.py` | 딕셔너리를 사용해 열린/닫힌 괄호 매칭 |
| `bracket_matching_ascii.py` | 아스키코드 기반 괄호 비교 |
| `a1_bracket_matching.py` | 괄호 검사 기본 구현 |

> 열린 괄호는 push, 닫힌 괄호는 pop 후 짝이 맞는지 확인

---

### ✅ 재귀 함수 예제

| 파일명 | 내용 |
|--------|------|
| `recursive_countdown.py` | 숫자를 0까지 재귀적으로 감소시켜 출력 |
| `recursive_factorial.py` | 재귀를 통한 팩토리얼 계산 |
| `recursive_fibonacci.py` | 재귀로 피보나치 수열 구현 |
| `recursive_sum.py` | 1부터 n까지의 합 계산 |
| `recursive_postorder_print.py` | 이진 트리의 후위 순회 출력 |
| `reverse_digits_recursive.py` | 숫자를 재귀적으로 뒤집어 출력 |

---

### ✅ 정렬 알고리즘

| 파일명 | 설명 |
|--------|------|
| `selection_sort.py` | 선택 정렬 기본 구현 (반복문 방식) |
| `selection_sort_recursive.py` | 선택 정렬 재귀 방식 구현 |

---

### ✅ 이진 탐색

| 파일명 | 설명 |
|--------|------|
| `binary_search_recursive.py` | 재귀적으로 구현한 이진 탐색 알고리즘 |

---

## 💡 정리 포인트

- 스택은 괄호 검사 등 LIFO 구조를 요구하는 문제에 필수적
- 재귀는 문제를 부분 문제로 나누는 방식으로, 종료 조건 설정이 핵심
- 선택 정렬은 간단하지만 비효율적인 O(n²) 정렬 알고리즘
- 이진 탐색은 정렬된 데이터에 대해 매우 빠른 탐색을 제공함

---

📂 실습 파일:
- 괄호 검사:  
  `a1_bracket_matching.py`, `bracket_matching_stack.py`, `bracket_matching_dict.py`, `bracket_matching_ascii.py`

- 재귀 함수:  
  `recursive_countdown.py`, `recursive_factorial.py`, `recursive_fibonacci.py`, `recursive_sum.py`,  
  `recursive_postorder_print.py`, `reverse_digits_recursive.py`

- 정렬 알고리즘:  
  `selection_sort.py`, `selection_sort_recursive.py`

- 이진 탐색:  
  `binary_search_recursive.py`

✍️ 과제:
- 다양한 괄호 조합 검사 구현 (예: (), {}, [])
- 반복문 기반 선택 정렬과 재귀 버전 비교
- 피보나치 수열을 **DP 방식**으로 개선해보기

---

**_다음 주는 DFS 기반의 그래프 탐색 문제로 이어집니다._**