# 재귀적으로 호출 후 출력하는 함수 (후위 순회 형태)
def GetSome(count):
    if count == 0:
        return  # 종료 조건: count가 0이면 재귀 중단
    GetSome(count - 1)  # 먼저 재귀 호출
    print("재귀호출 %d" % count)  # 재귀 복귀하면서 출력

# 3부터 시작
GetSome(3)

### 재귀 호출이 끝난 뒤에 출력하는 방식으로 일종의 후위 순회 구조입니다.