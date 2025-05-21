# 문자열로 구성된 숫자 리스트
data = ['1', '2', '3']

# 최종 숫자를 저장할 변수 초기화
val = 0

# 각 문자열을 정수로 변환하며 자릿수를 반영해 합산
for i in range(len(data)):
    val = val * 10 + int(data[i])  # 자릿수 올리고 현재 숫자 추가

# 결과 출력: 123
print(val)