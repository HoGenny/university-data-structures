import sys
sys.stdin = open('input.txt', 'r')

# 문자열에서 대문자와 소문자의 개수를 세는 함수
def getSome(s):
    d = {'대문자': 0, '소문자': 0}
    for letter in s:
        # 아스키 범위를 활용한 대소문자 판별
        if 'A' <= letter <= 'Z':
            d['대문자'] += 1
        elif 'a' <= letter <= 'z':
            d['소문자'] += 1
    return d

# 분석할 문자열
data = 'Hello World'

# 대문자/소문자 개수 계산
ans = getSome(data)

# 결과 출력
print(f"대문자 {ans['대문자']}, 소문자 {ans['소문자']}")