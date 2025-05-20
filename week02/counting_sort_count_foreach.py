# 정수 리스트 정의
data = [0, 4, 1, 3, 1, 2, 4, 1]

# 리스트에서 최댓값을 찾아서 count 배열 크기 설정
iamMax = max(data)

# 각 숫자의 빈도수를 저장할 카운트 배열 생성
count = [0] * (iamMax + 1)

# for-each 스타일로 리스트의 각 요소에 대해 카운트 수행
for now in data:
    count[now] += 1

# 결과 출력: 숫자별 등장 횟수 (인덱스 = 숫자, 값 = 빈도수)
print(count)  # 예: [1, 3, 1, 1, 2] → 1은 3번, 4는 2번 등장