# 정렬된 리스트 정의
data = [2, 4, 7, 9, 11, 19, 23]

# 찾고자 하는 값
key = 9

# 이진 탐색 범위 설정
start = 0
end = len(data) - 1

# 이진 탐색 시작
while start <= end:
    mid = (start + end) // 2  # 중간 인덱스 계산

    if data[mid] == key:
        print("찾았다")  # 원하는 값을 찾은 경우
        break
    elif data[mid] > key:
        end = mid - 1  # 왼쪽 반쪽 탐색
    else:
        start = mid + 1  # 오른쪽 반쪽 탐색

### 이진 탐색 알고리즘입니다.