import sys
sys.stdin = open("input.txt", 'r')

# 병합 정렬 함수 (분할)
def mergeSort(data):
    if len(data) <= 1:
        return data  # 기저 조건: 원소 1개면 정렬된 상태
    mid = len(data) >> 1
    left = mergeSort(data[:mid])
    right = mergeSort(data[mid:])
    return merge(left, right)

# 병합 함수 (두 정렬된 리스트 합치기)
def merge(left, right):
    result = []
    i, j = 0, 0

    # 왼쪽/오른쪽 리스트를 오름차순으로 병합
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 값들 추가
    result += left[i:]
    result += right[j:]

    return result

# 입력 처리
N = int(input())
nums = [int(input()) for _ in range(N)]

# 병합 정렬 수행
sorted_nums = mergeSort(nums)

# 결과 출력
for num in sorted_nums:
    print(num)

### 백준 10989. 수 정렬하기 3