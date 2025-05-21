# 재귀를 사용한 팩토리얼 함수 정의
def factorial(n):
    if n == 1:
        return 1  # 종료 조건: 1! = 1
    return n * factorial(n - 1)  # n! = n × (n-1)!

# 예시: 5! = 5×4×3×2×1 = 120
print(factorial(5))

### 재귀를 통해 팩토리얼을 계산하는 예제입니다.