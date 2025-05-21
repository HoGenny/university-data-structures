# 📌 12주차 - 문자열 알고리즘 (회문, 문자열 검색)

이번 주는 문자열을 다루는 다양한 알고리즘을 실습했습니다.  
**회문 판별(Palindrome)**과 **문자열 검색(String Matching)** 알고리즘(KMP, 라빈-카프 등)을 다뤘습니다.

---

## 📚 학습 내용

### ✅ 회문(Palindrome) 판별
- 문자열이 앞뒤로 동일한지 확인
- 슬라이싱, 리스트 비교, 반복문 활용 등 다양한 방식으로 구현

### ✅ 문자열 검색 알고리즘
- `find()`, `count()` 같은 기본 내장 함수
- KMP(Knuth-Morris-Pratt) 알고리즘
- 라빈-카프(Rabin-Karp) 알고리즘

---

## 🧪 실습 파일 설명

### ▶ `palindrome_check_list.py`
- 리스트 슬라이싱을 활용한 회문 판별

### ▶ `palindrome_check_reversed.py`
- 문자열을 `[::-1]`로 뒤집어 회문인지 확인

### ▶ `(a1)a2_palindrome_longest.py`
- 문자열 내 최장 회문 부분 문자열 찾기 (브루트포스 방식)

---

### ▶ `string_find_examples.py`
- 문자열 내 특정 패턴 찾기: `find()`, `rfind()`

### ▶ `string_count_examples.py`
- 문자열 내 특정 문자/패턴 개수 세기: `count()`

---

### ▶ `kmp_prefix_table.py`
- KMP 알고리즘에서 접두사 테이블(prefix table) 구성 구현

### ▶ `kmp_custom_search.py`
- 접두사 테이블을 이용한 KMP 문자열 검색 전체 구현

---

### ▶ `rabin_karp_1.py` & `rabin_karp_2.py`
- 해시를 이용한 문자열 검색 방법인 라빈-카프 알고리즘 구현

---

### ▶ `reverse_list_inplace.py`
- 리스트를 in-place 방식으로 뒤집는 방법 실습

---

## 💡 정리

| 알고리즘 | 시간 복잡도 | 특징 |
|----------|-------------|------|
| 슬라이싱 회문 | O(n) | 간단한 구현 |
| KMP | O(n + m) | 접두사 테이블 이용해 효율적 검색 |
| 라빈-카프 | O(n + m), 해시 충돌 시 O(nm) | 해시 기반 빠른 매칭 가능 |
| 브루트포스 회문 탐색 | O(n^3) | 비교적 느리지만 구현 쉬움 |

---

📂 실습 파일:  
`palindrome_*.py`, `string_*.py`, `kmp_*.py`, `rabin_karp_*.py`, `reverse_list_inplace.py`

✍️ 과제:
- SWEA 1216. [S/W 문제해결 기본] 3일차 - 회문2