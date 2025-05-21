import sys
sys.stdin = open('input.txt', 'r')

# 실패 함수(Pi 배열) 생성
def makePi():
    Pi[0] = -1
    i, j = 0, 1
    while j < howMany - 1:
        if pattern[i] == pattern[j]:
            Pi[j + 1] = Pi[j] + 1
            i += 1
            j += 1
        elif pattern[j] == pattern[0]:
            Pi[j + 1] = 1
            i = 1
            j += 1
        else:
            Pi[j + 1] = 0
            i = 0
            j += 1

# 패턴과 텍스트 입력
pattern = input()
Text = input()
howMany = len(pattern)
Pi = [0] * howMany

# 실패 함수 계산
makePi()

# 검색 시작
textI = 0
isDone = False

while textI < len(Text) - howMany + 1:
    k = 0
    for pti in range(howMany):
        if Text[textI] == pattern[pti]:
            k += 1
            textI += 1
            pti += 1
        else:
            break
    if k == howMany:
        print(textI - howMany)
        isDone = True
        break
    textI = textI + k - Pi[k]

# 결과 없을 경우
if not isDone:
    print("None")