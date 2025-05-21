# 두 정렬된 리스트를 병합하는 함수
def merge(left, right):
    result = []       # 결과 리스트
    i, j = 0, 0        # 각 리스트의 인덱스 초기화

    # 양쪽 리스트 모두 아직 비교할 원소가 있을 경우
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])  # 더 작은 쪽을 결과에 추가
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 요소들 추가 (하나만 남아있음)
    result += right[j:]
    result += left[i:]

    return result

# 테스트용 리스트
left = [3, 20, 23, 54]
right = [1, 5, 25, 75]

# 병합 결과 출력
print(merge(left, right))
