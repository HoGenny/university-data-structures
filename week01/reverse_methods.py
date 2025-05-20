# 1부터 6까지의 숫자를 담은 리스트 생성
Data = [i for i in range(1, 7)]

# 리스트의 길이 저장
howmany = len(Data)

# 방법 1: 인덱스를 이용한 리스트 뒤집기 (수동으로 스왑)
for i in range(howmany // 2):
    # 첫 요소와 마지막 요소부터 순차적으로 교환
    Data[i], Data[howmany - 1 - i] = Data[howmany - 1 - i], Data[i]

# 결과 출력
print(Data)  # [6, 5, 4, 3, 2, 1]

# 방법 2: 내장 함수 reverse() 사용 (원본 리스트를 직접 뒤집음)
Data.reverse()
print(Data)  # [1, 2, 3, 4, 5, 6]

# 방법 3: 슬라이싱을 이용한 리스트 뒤집기 (새 리스트를 생성함)
print(Data[::-1])  # [6, 5, 4, 3, 2, 1]