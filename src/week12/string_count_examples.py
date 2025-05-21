# 문자열 정의
str = 'this is sample string'

# 'i'가 문자열 전체에서 몇 번 나오는지 세기
c1 = str.count('i')  # 전체 문자열 기준

# 'i'가 index 10부터 끝까지 몇 번 나오는지 세기
c2 = str.count('i', 10)  # 부분 문자열: str[10:]

# 'i'가 index 0부터 10 전까지 몇 번 나오는지 세기
c3 = str.count('i', 0, 10)  # 부분 문자열: str[0:10]

# 결과 출력
print(c1)  # 전체에서 'i'의 개수
print(c2)  # 인덱스 10부터 끝까지의 'i' 개수
print(c3)  # 인덱스 0~9까지의 'i' 개수
