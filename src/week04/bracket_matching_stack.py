# 검사할 괄호 리스트
data = ['(', '(', ')', ')']

# 여는 괄호를 담을 스택
stack = []

# 정답 변수: 1이면 올바른 괄호쌍, 0이면 틀림
ans = 0

# 괄호 쌍이 맞는지 여부
isMatched = True

# 검사할 괄호가 남아 있는 동안 반복
while data:
    now = data.pop(0)  # 맨 앞의 괄호를 꺼냄

    # 여는 괄호일 경우 스택에 추가
    if now in '({<[':
        stack.append(now)

    # 닫는 괄호일 경우
    elif stack:
        what = stack.pop()  # 마지막으로 연 괄호
        # 현재 닫는 괄호와 스택에서 꺼낸 괄호가 짝이 맞는지 검사
        if now == ')' and what != '(' or \
           now == '>' and what != '<' or \
           now == '}' and what != '{' or \
           now == ']' and what != '[':
            break  # 짝이 안 맞으면 종료

    else:
        # 닫는 괄호가 나왔지만 스택이 비어 있으면 실패
        isMatched = False
        break

# 모든 괄호 쌍이 맞고 스택이 비어있다면 정답 처리
if isMatched and not stack:
    ans = 1

# 결과 출력
print(ans)  # 1이면 맞음, 0이면 틀림

### 스택 기반 괄호 검사 알고리즘입니다.