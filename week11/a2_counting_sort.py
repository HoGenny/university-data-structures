import sys
sys.stdin = open("input.txt", "r")

# 계수 정렬 출력 함수
def countSort():
    for num in range(1, 10001):          # 숫자 범위 1~10000
        if count[num] != 0:
            for _ in range(count[num]):  # 해당 숫자의 개수만큼 출력
                print(num)

# 입력 개수
N = int(input())

# 숫자 출현 횟수를 저장할 배열
count = [0] * 10001

# 입력 받기 및 카운트 배열 채우기
for _ in range(N):
    num = int(input())
    count[num] += 1

# 정렬 결과 출력
countSort()

### 백준 10989. 수 정렬하기 3