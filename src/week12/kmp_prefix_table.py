import sys
sys.stdin = open('input.txt', 'r')

# KMP의 접두사 배열(Pi) 생성 함수
def makePi():
    Pi[0] = -1            # 첫 인덱스는 관례적으로 -1로 시작
    i, j = 0, 1           # i: 접두사 포인터, j: 접미사 포인터

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

# 패턴 입력
pattern = input()
howMany = len(pattern)
Pi = [0] * howMany

# Pi 배열 생성
makePi()

# 결과 출력
print(Pi)
