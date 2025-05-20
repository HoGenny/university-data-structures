# 문자열을 리스트로 변환
data = list("radar")

# 리스트를 뒤집어서 새 리스트 생성
reData = list(reversed(data))

# 원본과 뒤집은 것이 같은지 비교
if data == reData:
    print("회문")
else:
    print("아님")


# 간단한 문자열 버전
# text = "radar"
# if text == text[::-1]:
#     print("회문")
# else:
#     print("아님")