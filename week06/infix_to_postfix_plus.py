# 중위표기식 (Infix Expression)
data = '3+4+2'

# 연산자 저장용 스택
stack = []

# 후위표기식 결과 리스트
postFix = []

# 중위표기식을 순회하며 후위표기식으로 변환
for now in data:
    if '0' <= now <= '9':
        # 숫자는 바로 출력 (후위표기식에 추가)
        postFix.append(now)
    else:
        # 연산자는 스택에 push
        stack.append(now)

# 남은 연산자들을 후위표기식에 추가
while stack:
    postFix.append(stack.pop())

# 결과 출력
print(postFix)

### 단순한 중위 -> 후위 표기 변환기입니다.