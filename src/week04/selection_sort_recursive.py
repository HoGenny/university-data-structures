# 선택 정렬을 재귀적으로 구현한 함수
def cSearch(data, position = 0):
    # 종료 조건: 마지막 요소에 도달하면 정렬 완료
    if position == len(data) - 1:
        return

    wheremin = position  # 현재 위치를 최소값 위치로 가정

    # 현재 위치 이후 중 가장 작은 값을 찾음
    for now in range(position + 1, len(data)):
        if data[now] < data[wheremin]:
            wheremin = now

    # 현재 위치와 가장 작은 값 위치를 교환
    data[position], data[wheremin] = data[wheremin], data[position]

    # 다음 위치에 대해 재귀 호출
    cSearch(data, position + 1)

# 정렬할 리스트
data = [3, 2, 5, 4, 1]

# 정렬 수행
cSearch(data)

# 결과 출력
print(data)

### 선택 정렬을 재귀 함수로 구현한 예제입니다.