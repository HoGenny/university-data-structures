import sys
sys.stdin = open("input.txt", 'r')

# 괄호 쌍 정의 (닫는 괄호 → 여는 괄호)
pare = {'>': '<', ')': '(', '}': '{', ']': '['}

# 10개의 테스트케이스 수행
for tc in range(10):
    T = int(input())         # 문자열 길이 (사용 X)
    N = input()              # 괄호 문자열 입력
    stack = []               # 여는 괄호 저장용 스택
    ans = 0
    isMatched = True

    # 문자열을 왼쪽부터 순회
    for now in N:
        if now in pare.values():
            stack.append(now)  # 여는 괄호는 스택에 저장
        elif now in pare:      # 닫는 괄호일 경우
            if stack and stack[-1] == pare[now]:
                stack.pop()    # 짝이 맞으면 스택에서 제거
            else:
                isMatched = False
                break

    # 짝이 모두 맞고 스택이 비어있으면 정답 처리
    if isMatched and not stack:
        ans = 1

    # 결과 출력 (SWEA 형식)
    print(f'#{tc+1} {ans}')

### 1218. [S/W 문제해결 기본] 4일차 - 괄호 짝짓기