# 빠른 거듭제곱 계산 함수
def getSome(a, b):
    if b == 1:
        return a  # a^1 = a

    halfPower = getSome(a, b // 2)  # a^(b//2)

    if b & 1:  # b가 홀수일 경우
        return halfPower * halfPower * a  # a^(b//2) * a^(b//2) * a
    else:      # b가 짝수일 경우
        return halfPower * halfPower  # a^(b//2) * a^(b//2)

# 2^8 = 256 출력
print(getSome(2, 8))

### 재귀적으로 지수를 절반으로 나누는 분할 정복 기법을 사용하여 일반적인 곱셈 반복보다 시간 복잡도를 줄입니다.