# 숫자 리스트 (자릿수 나열)
text = [3, 1, 4, 1, 5, 1, 2]
pattern = 151

# 패턴의 자릿수
howmany = len(str(pattern))

# 초기 윈도우 값 계산 (첫 howmany개의 숫자로 만든 정수)
val = 0
for now in range(howmany):
    val = val * 10 + text[now]

# 자릿수 앞자리에 해당하는 가중치 (ex: 151이면 100)
digit = 10 ** (howmany - 1)

# 슬라이딩 윈도우 방식으로 매번 새로 계산하지 않고 갱신
for i in range(1, len(text) - howmany + 1):
    val -= digit * text[i - 1]         # 맨 앞 자리 제거
    val = val * 10 + text[i + howmany - 1]  # 새 뒷자리 추가

    if val == pattern:
        print("found")
