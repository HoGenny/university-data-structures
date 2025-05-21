# 퀵 정렬 실행 함수
def quickSort(_from, _to):
    if _from < _to:  # 정렬할 구간이 2개 이상일 때
        pivot = partition(_from, _to)  # 분할 수행
        quickSort(_from, pivot - 1)    # 왼쪽 부분 정렬
        quickSort(pivot + 1, _to)      # 오른쪽 부분 정렬

# 파티션 함수 (Hoare 방식)
def partition(_from, _to):
    where = _from             # 기준점 인덱스
    princess = data[where]    # 피벗 값
    left = _from
    right = _to

    while left < right:
        while left < len(data) and data[left] <= princess:
            left += 1
        while data[right] > princess and right >= 0:
            right -= 1
        if left < right:
            data[left], data[right] = data[right], data[left]

    # 피벗과 오른쪽 포인터 교환
    data[where], data[right] = data[right], data[where]
    return right  # 새로운 피벗 위치 반환

# 정렬 대상 리스트
data = [3, 2, 4, 6, 9, 1, 8, 7, 5]

# 퀵 정렬 실행
quickSort(0, len(data) - 1)

# 결과 출력
print(data)
