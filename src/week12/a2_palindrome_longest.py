import sys
sys.stdin = open('input.txt', 'r')

# 총 10개의 테스트 케이스
for _ in range(10):
    data = []
    max_lenth = 1

    tc = int(input())  # 테스트 케이스 번호 입력
    data = [input() for _ in range(100)]  # 100줄 입력

    # 길이 1부터 100까지 가능한 회문 길이 모두 검사
    for lenth in range(1, 101):
        for i in range(100):
            for j in range(100 - lenth + 1):

                # 가로 방향 부분 문자열 추출
                temp1 = data[i][j:j + lenth]
                if temp1 == temp1[::-1]:  # 회문 검사
                    max_lenth = lenth

                # 세로 방향 부분 문자열 추출
                if i <= 100 - lenth:
                    temp2 = [data[i + k][j] for k in range(lenth)]
                    if temp2 == temp2[::-1]:  # 회문 검사
                        max_lenth = lenth

    print(f"#{tc} {max_lenth}")

### 1216. [S/W 문제해결 기본] 3일차 - 회문2