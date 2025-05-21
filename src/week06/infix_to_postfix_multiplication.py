# 중위표기식 문자열
data = '5+3*4/2'

# 연산자 저장용 스택
stack = []

# 후위표기식 결과 저장 리스트
postFix = []

# 연산자 우선순위 정의
priority = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

# 중위표기식을 후위표기식으로 변환
for now in data:
    if '0' <= now <= '9':
        # 숫자는 그대로 출력
        postFix.append(now)
    else:
        # 스택에 있는 연산자가 현재 연산자보다 우선순위가 높거나 같으면 꺼냄
        while stack and priority[stack[-1]] >= priority[now]:
            postFix.append(stack.pop())
        stack.append(now)

# 남은 연산자를 후위표기식에 추가
while stack:
    postFix.append(stack.pop())

# 결과 출력
print(postFix)
