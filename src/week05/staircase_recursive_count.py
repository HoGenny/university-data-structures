# 모든 경우의 수를 저장할 전역 변수
def GetSome(here):
    global ans

    # 종료 조건: 정확히 목표에 도달한 경우
    if here == howmany:
        ans += 1
        return

    # 종료 조건: 목표를 넘은 경우 (잘못된 경로)
    if here > howmany:
        return

    # 한 칸 가는 경우
    GetSome(here + 1)

    # 두 칸 가는 경우
    GetSome(here + 2)

# 초기 조건
ans = 0
howmany = 3  # 목표 위치 (예: 3칸 계단)

# 탐색 시작
GetSome(0)

# 가능한 모든 경우의 수 출력
print(ans)

### 계단 오르기 문제입니다.
### howmany 칸을 1칸 또는 2칸씩 이동해 도달하는 모든 방법의 수를 재귀로 계산합니다.