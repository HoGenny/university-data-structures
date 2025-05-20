# 재귀적으로 숫자를 감소시키며 출력하는 함수
def GetSome(count):
    if count == 0:
        return  # 종료 조건: count가 0이면 더 이상 호출하지 않음
    print("재귀 호출 %d" % count)
    GetSome(count - 1)  # count를 1 줄여 재귀 호출

# 3부터 시작해 재귀 호출
GetSome(3)

### 재귀 호출의 흐름을 이해하기 위한 간단한 카운트다운 예제입니다.