# 결과값과 자리수 추적용 전역 변수
ans = 0       # 뒤집힌 숫자를 저장
digit = 1     # 현재 자리수 (1의 자리부터 시작)

# 숫자를 뒤집는 재귀 함수
def GetSome(num):
    global ans
    global digit

    if num > 0:
        GetSome(int(num / 10))              # 다음 자리 재귀 호출
        ans += (num % 10) * digit           # 현재 자리수 값 더함
        digit *= 10                         # 자리수 증가 (1 → 10 → 100 ...)
    return

# 예시 입력: 321 → 출력: 123
GetSome(321)
print(ans)

### 숫자 321을 입력받아 자릿수를 반대로 뒤집어 123으로 만드는 재귀 알고리즘입니다.