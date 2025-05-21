# 정렬 대상 리스트
data = [2, 5, 3, 4, 1]

# 삽입 정렬 수행
for i in range(1, len(data)):
    key = data[i]      # 현재 비교할 값
    j = i - 1

    # key보다 큰 값을 오른쪽으로 한 칸씩 이동
    while j >= 0 and key < data[j]:
        data[j + 1] = data[j]
        j = j - 1

    # key를 알맞은 위치에 삽입
    data[j + 1] = key

# 정렬 결과 출력
print(data)

### 삽입 정렬 알고리즘입니다.