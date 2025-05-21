# 리스트를 입력받아 정렬된 리스트를 반환하는 퀵 정렬 함수
def quickSort(data):
    # 원소가 1개 이하이면 그대로 반환 (종료 조건)
    if len(data) <= 1:
        return data

    # 첫 원소를 피벗으로 설정
    pivot = data[0]
    less, equal, greater = [], [], []

    # 모든 원소를 피벗 기준으로 세 그룹으로 분할
    for _ in range(len(data)):
        each = data.pop()  # 맨 뒤에서 하나씩 꺼냄
        if each < pivot:
            less.append(each)
        elif each > pivot:
            greater.append(each)
        else:
            equal.append(each)

    # 재귀적으로 양쪽을 정렬하고 합치기
    return quickSort(less) + equal + quickSort(greater)

# 테스트
print(quickSort(data = [3, 2, 4, 6, 9, 1, 8, 7, 5]))
