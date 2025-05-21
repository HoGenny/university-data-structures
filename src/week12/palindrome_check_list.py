# 리스트 정의
data = [10, 20, 30, 20, 10]

# 회문 여부를 저장할 변수
isPalin = True

# 리스트의 절반만 비교 (양쪽에서 중앙으로 이동)
for now in range(len(data) >> 1):  # len(data) // 2와 동일
    if data[now] != data[-1 - now]:
        isPalin = False  # 하나라도 다르면 회문 아님
        break

# 결과 출력
print(isPalin)