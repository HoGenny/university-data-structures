# 데이터 리스트 초기화
Data = [3, 2, 5, 4, 1]

# 최댓값을 리스트의 첫 번째 요소로 초기화
max = Data[0]

# 최댓값의 위치를 저장할 변수 (-1은 초기값으로, 업데이트되면 인덱스로 변경됨)
wheremax = -1

# 리스트의 모든 요소를 순회하면서
for now in range(len(Data)):
    # 현재 요소가 현재까지의 최댓값보다 크다면
    if Data[now] > max:
        max = Data[now]        # 최댓값 업데이트
        wheremax = now         # 최댓값의 위치(인덱스) 저장

# 최댓값과 그 위치 출력
print(max, wheremax)