# 정렬할 데이터 리스트
data = [0, 4, 1, 3, 1, 2, 4, 1]

# 데이터 중 최댓값 확인 (count 배열 크기를 위한 기준)
iamMax = max(data)

# 각 숫자의 빈도수를 저장할 배열 (0으로 초기화)
count = [0] * (iamMax + 1)

# 1단계: 빈도수 세기
for now in data:
    count[now] += 1

# 2단계: 누적합 생성 (각 숫자의 정렬 위치 계산)
for i in range(1, len(count)):
    count[i] += count[i - 1]

# 3단계: 결과를 담을 리스트 초기화
result = [0] * len(data)

# 4단계: 원본 데이터를 역순으로 순회하며 정렬된 위치에 값 배치
for now in data[::-1]:
    count[now] -= 1
    result[count[now]] = now

# 결과 출력: 정렬된 리스트
print(result)  # [0, 1, 1, 1, 2, 3, 4, 4]

### 완전한 카운팅 소트 구현입니다.