# 괄호 쌍을 정의한 딕셔너리 (key: 닫는 괄호, value: 여는 괄호)
pare = {'>': '<', ')': '(', '}': '{', ']': '['}

# 검사할 괄호 시퀀스
data = ['(', '(', ')', ')']

# 스택: 여는 괄호를 저장
stack = []

# 중간 확인용 변수 (사용되진 않음)
what = []

# 결과 변수
ans = 0

# 괄호 쌍이 올바른지 판별
isMatched = True

# 모든 괄호를 순회
while data:
    now = data.pop(0)

    if now in pare.values():
        # 여는 괄호는 스택에 저장
        stack.append(now)
    elif stack and stack[-1] == pare[now]:
        # 닫는 괄호가 나왔고, 스택 마지막이 쌍이 맞으면 pop
        what = stack.pop()
    else:
        # 닫는 괄호가 쌍이 안 맞거나 스택이 비어있다면 틀림
        isMatched = False
        break

# 모든 괄호 쌍이 맞고 스택도 비어 있으면 정답 처리
if isMatched and not stack:
    ans = 1

# 결과 출력
print(ans)

### 딕셔너리 활용 괄호 검사 알고리즘입니다.