# 정수 값 설정
val = 123

# 계산용 임시 변수에 복사
temp = val

# 자릿수를 세기 위한 변수 초기화
howmany = 0

# 정수의 자릿수 계산
while temp:
    howmany += 1
    temp //= 10  # 한 자리씩 줄이면서 자릿수 카운트

# 자릿수만큼 0으로 채워진 리스트 생성
data = [0] * howmany

# 가장 낮은 자리부터 문자열로 변환하여 리스트에 채움
while howmany:
    howmany -= 1
    data[howmany] = str(val % 10)  # 마지막 자리 수를 문자열로 저장
    val //= 10                     # 다음 자리 수로 이동

# 결과 출력: ['1', '2', '3']
print(data)