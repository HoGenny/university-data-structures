import sys
sys.stdin = open("input.txt", "r")

data = []

# 퀵 정렬 함수 (재귀)
def quickSort(_from, _to):
    if _from < _to:
        pivot = partition(_from, _to)
        quickSort(_from, pivot - 1)
        quickSort(pivot + 1, _to)

# 파티션 함수 (Hoare 방식)
def partition(_from, _to):
    where = _from
    princess = data[where]
    left = _from + 1
    right = _to

    while True:
        # 왼쪽 포인터: 피벗 이하일 때까지 이동
        while left <= right and data[left] <= princess:
            left += 1
        # 오른쪽 포인터: 피벗보다 클 때까지 이동
        while left <= right and data[right] > princess:
            right -= 1
        # 포인터가 교차되면 반복 종료
        if left > right:
            break
        # 두 값 교환
        data[left], data[right] = data[right], data[left]

    # 피벗과 오른쪽 포인터 위치 교환
    data[where], data[right] = data[right], data[where]
    return right  # 새로운 피벗 위치 반환

# 입력 받기
N = int(input())
for _ in range(N):
    data.append(int(input()))

# 정렬 수행
quickSort(0, len(data) - 1)

# 결과 출력
for num in data:
    print(num)

### 백준 10989. 수 정렬하기 3