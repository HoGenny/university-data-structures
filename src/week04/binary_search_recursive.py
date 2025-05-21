# 재귀적으로 이진 탐색을 수행하는 함수
def Bsearch(start, end):
    if start > end:
        return False  # 탐색 실패

    mid = (start + end) // 2

    if key == data[mid]:
        return True  # 탐색 성공
    elif key < data[mid]:
        return Bsearch(start, mid - 1)  # 왼쪽 반 구간 탐색
    else:
        return Bsearch(mid + 1, end)  # 오른쪽 반 구간 탐색

# 정렬된 데이터 리스트
data = [2, 4, 7, 9, 11, 19, 23]

# 찾고자 하는 값
key = 7

# 이진 탐색 수행 및 결과 출력
print(Bsearch(0, len(data) - 1))  # True 출력

### 이진 탐색을 재귀 함수로 구현한 예제입니다.