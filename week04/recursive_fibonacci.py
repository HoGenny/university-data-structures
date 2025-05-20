# 재귀적으로 피보나치 수열을 구하는 함수
def Fibonacci(n):
    if n == 0 or n == 1:
        return 1  # 기본 항: F(0) = 1, F(1) = 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)  # F(n) = F(n-1) + F(n-2)

# 10번째 피보나치 수 출력 (F(10))
print(Fibonacci(10))

### 재귀로 피보나치 수열을 계산하는 예제입니다.