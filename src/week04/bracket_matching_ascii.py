# 아스키 코드 기반 괄호 쌍 매핑을 위한 배열 생성 (0~127까지)
pare = [0] * 128

# 닫는 괄호 → 여는 괄호 매핑 (아스키 코드 기준)
pare[ord(')')] = ord('(')
pare[ord(']')] = ord('[')
pare[ord('>')] = ord('<')
pare[ord('}')] = ord('{')

# 검사할 괄호 리스트
data = ['(', '(', ')', ')']

# 여는 괄호 저장용 스택
stack = []

# 결과 변수
ans = 0
isMatched = True

# 괄호 검사 시작
while data:
    now = ord(data.pop(0))  # 현재 괄호의 아스키 코드

    # 여는 괄호일 경우
    if now in map(ord, '({<['):
        stack.append(now)

    # 닫는 괄호일 경우
    elif stack:
        what = stack.pop()
        # 매핑이 맞지 않으면 오류
        if pare[now] != what:
            break

    # 스택이 비어 있는데 닫는 괄호가 온 경우
    else:
        isMatched = False
        break

# 모든 쌍이 맞고 스택이 비어 있으면 유효한 괄호열
if isMatched and not stack:
    ans = 1

# 결과 출력 (1: 올바름, 0: 틀림)
print(ans)

### ASCII 코드 기반 괄호 검사 알고리즘입니다.
### ord()와 배열 인덱싱을 활용해 매우 빠른 매핑이 가능하므로, 속도에 최적화된 괄호 검사입니다.