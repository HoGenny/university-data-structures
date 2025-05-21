# 재귀 병합 정렬 함수
def mergeSort(data):
    # 원소가 1개 이하인 경우 그대로 반환
    if len(data) <= 1:
        return data

    # 중간 위치 계산 (절반으로 분할)
    mid = len(data) >> 1
    left = data[:mid]
    right = data[mid:]

    # 재귀적으로 좌우 정렬
    left = mergeSort(left)
    right = mergeSort(right)

    # 정렬된 두 리스트 병합
    return merge(left, right)

# 두 정렬된 리스트를 하나로 병합
def merge(left, right):
    result = []
    i, j = 0, 0

    # 작은 값을 차례대로 결과 리스트에 추가
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 원소 추가
    result += left[i:]
    result += right[j:]

    return result

# 정렬 대상 리스트
data = [38, 43, 27, 3, 9, 82, 10]

# 병합 정렬 실행 및 출력
print(mergeSort(data))
