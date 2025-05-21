# 중위표기식 문자열
data = '3+4-2'

# 연산자 저장용 스택
stack = []

# 결과로 만들 후위표기식 리스트
postFix = []

# 중위표기식 순회
for now in data:
    if '0' <= now <= '9':
        # 숫자는 그대로 출력
        postFix.append(now)
    else:
        # 연산자가 나오면 스택에 있는 연산자 모두 꺼냄 (우선순위 고려 안 함)
        while stack:
            postFix.append(stack.pop())
        stack.append(now)

# 남은 연산자 모두 출력
while stack:
    postFix.append(stack.pop())

# 결과 출력
print(postFix)