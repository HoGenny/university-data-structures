# 중위표기식 입력
data = '1+2*3+(4+5)/6'

# 스택 및 후위표기식 리스트 초기화
stack = []
postFix = []

# 연산자 우선순위: ISP (스택 내부), ICP (스택 외부)
ISP = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
ICP = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}

# 중위표기식 → 후위표기식 변환
for now in data:
    if '0' <= now <= '9':
        postFix.append(now)  # 숫자는 그대로 출력
    elif now == ')':
        # 여는 괄호 전까지 스택에서 꺼내기
        while stack[-1] != '(':
            postFix.append(stack.pop())
        stack.pop()  # '(' 제거
    else:
        # 연산자 또는 여는 괄호 처리
        if not stack:
            stack.append(now)
        elif ICP[now] > ISP[stack[-1]]:
            stack.append(now)
        else:
            while stack and ISP[stack[-1]] >= ICP[now]:
                postFix.append(stack.pop())
            stack.append(now)

# 남아 있는 연산자 후위표기식에 추가
while stack:
    postFix.append(stack.pop())

# 후위표기식 평가
stack = []
for now in postFix:
    if now.isdigit():
        stack.append(now)  # 숫자는 스택에 push
    else:
        b = int(stack.pop())
        a = int(stack.pop())
        if now == '+':
            stack.append(a + b)
        elif now == '-':
            stack.append(a - b)
        elif now == '*':
            stack.append(a * b)
        elif now == '/':
            stack.append(a / b)  # 실수 나눗셈

# 최종 계산 결과 출력
print(stack[-1])
