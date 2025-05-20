# 정렬할 리스트
data = [3, 2, 5, 4, 1]
howmany = len(data)

# 선택 정렬 수행
for position in range(howmany - 1):
    wheremin = position  # 현재 위치를 최소값 위치로 가정

    # 나머지 요소들 중에서 더 작은 값을 찾음
    for now in range(position + 1, howmany):
        if data[now] < data[wheremin]:
            wheremin = now  # 더 작은 값이 있다면 인덱스 갱신

    # 현재 위치와 가장 작은 값 위치를 교환
    data[position], data[wheremin] = data[wheremin], data[position]

# 정렬 결과 출력
print(data)

### 선택 정렬의 기본적인 예제입니다.