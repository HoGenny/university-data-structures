import sys
sys.stdin = open('input.txt', 'r')

# 총 10개의 테스트케이스 처리
for i in range(10):
    tc = int(input())       # 테스트케이스 번호 (실제 계산에는 사용되지 않음)
    data = input()          # 수식 문자열 입력

    # 연산자 스택과 후위표기식 결과 리스트
    stack = []
    postFix = []

    # 연산자 우선순위 (스택 안/밖 우선순위 구분)
    ISP = {'+':1, '-':1, '*':2, '/':2, '(':0}  # In-Stack Priority
    ICP = {'+':1, '-':1, '*':2, '/':2, '(':3}  # Incoming Priority

    # 중위 → 후위 변환
    for now in data:
        if '0' <= now <= '9':        # 숫자는 후위표기식에 바로 추가
            postFix.append(now)
        elif now == ')':             # 닫는 괄호 처리
            while stack[-1] != '(':
                postFix.append(stack.pop())
            stack.pop()              # 여는 괄호 '(' 제거
        else:                        # 연산자 또는 여는 괄호
            if not stack:
                stack.append(now)
            elif ICP[now] > ISP[stack[-1]]:
                stack.append(now)
            else:
                while stack and ISP[stack[-1]] >= ICP[now]:
                    postFix.append(stack.pop())
                stack.append(now)

    # 스택에 남은 연산자 후위표기식에 추가
    while stack:
        postFix.append(stack.pop())

    # 후위표기식 계산
    stack = []
    for now in postFix:
        if now.isdigit():
            stack.append(now)  # 숫자는 스택에 추가
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

    # 결과 출력 (SWEA 포맷)
    print(f'#{i + 1} {int(stack[-1])}')  # 결과는 정수로 출력

### 1224. [S/W 문제해결 기본] 6일차 - 계산기3