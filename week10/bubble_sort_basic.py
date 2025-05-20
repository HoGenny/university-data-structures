# 정렬 대상 리스트
data = [2, 3, 5, 4, 1]

# 버블 정렬 알고리즘
# 총 (n-1)번 반복
for i in range(1, len(data)):
    # 인접한 두 원소를 비교하여 큰 값을 뒤로 보내는 과정
    for j in range(len(data) - 1):
        if data[j] > data[j + 1]:
            # 교환 (swap)
            data[j], data[j + 1] = data[j + 1], data[j]

# 정렬 결과 출력
print(data)

### 버블 정렬 알고리즘입니다.