# 하노이의 탑 재귀 해결 함수
def solveTowers(n, _from, _to, spare):
    if n > 0:
        # 1단계: n-1개의 원반을 보조 기둥으로 이동
        solveTowers(n - 1, _from, spare, _to)

        # 2단계: 가장 큰 원반(n번 원반)을 목적지로 이동
        print("%d번 원반을 %s에서 %s으로 옮김" % (n, _from, _to))

        # 3단계: n-1개의 원반을 보조 기둥에서 목적지로 이동
        solveTowers(n - 1, spare, _to, _from)

# 원반 개수
n = 3

# 'from' 기둥에서 'to' 기둥으로 옮기기 시작
solveTowers(n, 'from', 'to', 'spare')

### 이 코드는 하노이의 탑 문제를 재귀적 방식으로 해결합니다.
### 핵심 원리는 큰 원반을 옮기기 전, 작은 원반을 보조 기둥으로 옮겨야 한다는 것입니다.
### 이동 횟수는 2^n - 1번 입니다.