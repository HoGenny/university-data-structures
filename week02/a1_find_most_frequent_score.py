import sys

# 표준 입력을 input.txt 파일로 대체
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 수만큼 반복
for tc in range(1, int(input()) + 1):
    dummy = int(input())  # 보통 시험 번호나 필요 없는 값일 경우 사용됨
    data = list(map(int, input().split()))  # 점수 리스트 입력

    # 점수는 0~100 범위라고 가정하고 카운트 배열 생성
    count = [0] * 101

    # 각 점수의 등장 횟수 카운팅
    for now in data:
        count[now] += 1

    # 최빈값(max 빈도수) 및 그 점수(wheremax)를 찾기 위한 초기값 설정
    max = count[0]
    wheremax = -1

    # count 배열을 순회하며 가장 많이 나온 점수를 찾음
    # 같은 빈도수일 경우 높은 점수를 선택하기 위해 <= 사용
    for now in range(len(count)):
        if max <= count[now]:
            max = count[now]
            wheremax = now

    # 결과 출력 (SWEA 스타일 포맷)
    print(f"#{tc} {wheremax}")

### SWEA 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기