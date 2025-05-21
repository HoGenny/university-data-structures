# 정방향 리스트
data = [1, 2, 3, 4, 5]

# 양 끝 인덱스 설정
start = 0
end = len(data) - 1

# 투 포인터로 리스트 뒤집기
while start < end:
    # 양 끝 요소 교환
    data[start], data[end] = data[end], data[start]
    # 포인터 이동
    start += 1
    end -= 1

# 결과 출력
print(data)
