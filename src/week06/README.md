# 📌 6주차 - 수식 계산 (중위 → 후위 표기) & 경로 탐색

이번 주는 스택(Stack) 구조를 활용한 **중위표기식 계산**,  
그리고 **경로 추적 문제(사다리, 능력치 기반 이동)**를 실습했습니다.

---

## 📚 학습 내용

### ✅ 중위표기식 → 후위표기식 변환

| 항목 | 설명 |
|------|------|
| 중위표기식 (Infix) | A + B 형태, 연산자 우선순위 고려 필요 |
| 후위표기식 (Postfix) | A B + 형태, 스택으로 계산하기 용이 |
| 스택 사용 이유 | 연산자 우선순위와 괄호 처리를 쉽게 구현 |

> 참고: `+, -, *, /` 연산 우선순위 및 괄호 처리 중요

---

### ✅ 경로 탐색

- `사다리 경로 추적(Ladder Trace)`  
  - 위에서 아래로 경로를 따라가며 시작점 찾기
- `능력치 기반 최소 이동(min_steps_with_abilities)`  
  - 제한된 능력을 이용한 최소 거리 계산 (BFS or DP 방식)

---

## 🧪 실습 파일 설명

### ▶ 중위 → 후위 변환 및 계산 관련
- `infix_to_postfix_plus.py`: 덧셈 전용 후위 변환
- `infix_to_postfix_multiplication.py`: 곱셈 우선 적용
- `infix_to_postfix_left_to_minus.py`: 뺄셈 우선 처리
- `infix_to_postfix_eval.py`: 후위표기식 계산까지 구현
- `a2_evaluate_infix_expressions.py`: 다양한 중위 수식 계산기 (스택 기반)

### ▶ 경로 추적 / 게임 시뮬레이션
- `a1_ladder_trace.py`: 2차원 배열 기반 사다리 경로 추적
- `min_steps_with_abilities.py`: 주어진 능력치로 최소 이동거리 계산 문제

---

## 💡 정리 포인트

- 후위표기식 변환은 스택 구조의 대표적인 활용 예시
- 연산자 우선순위, 괄호, 좌우 결합성(associativity)을 구분해야 정확한 계산 가능
- 경로 추적 문제는 DFS/BFS와 같은 탐색 알고리즘 연습에 유용
- 실생활 시뮬레이션 형태의 문제는 알고리즘을 직관적으로 익힐 수 있음

---

📂 실습 파일:  
- `infix_to_postfix_*.py`, `a2_evaluate_infix_expressions.py`  
- `a1_ladder_trace.py`, `min_steps_with_abilities.py`

✍️ 과제:
- 후위표기식을 역변환(Infix)하는 함수 구현해보기
- 능력치가 달라지는 조건에서 최소 이동 구현 (점프 제한 등 확장)

---

**_다음 주는 DFS/BFS 탐색과 큐 구조로 넘어갑니다._**