# 주어진 숫자 n에 대한 팩토리얼 값을 반환하는 함수
def GetSome(n):
    s = 1
    for num in range(1, n + 1):
        s = s * num  # 누적 곱셈으로 팩토리얼 계산
    return s

# 입력값 a, b
a, b = 3, 4

# 각각의 팩토리얼 계산
getA = GetSome(a)  # 3! = 6
getB = GetSome(b)  # 4! = 24

# 두 팩토리얼의 곱 출력
print(getA * getB)  # 6 * 24 = 144