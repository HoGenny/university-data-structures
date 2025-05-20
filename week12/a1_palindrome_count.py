import sys
sys.stdin = open('input.txt', 'r')

# 총 10개의 테스트 케이스
for tc in range(1, 11):
    count = 0
    lenth = int(input())  # 찾을 회문의 길이
    data = []

    # 8x8 글자 격자 입력
    for _ in range(8):
        line = input().strip()
        data.append(list(line))

    # 모든 행과 열에서 길이 lenth의 회문 찾기
    for i in range(8):  # 행과 열을 한 번에 돌림
        for j in range(8 - lenth + 1):  # 시작 위치 제한

            # 가로 회문 추출
            temp1 = data[i][j:j + lenth]

            # 세로 회문 추출
            temp2 = [data[j + k][i] for k in range(lenth)]

            # 각각 뒤집은 결과
            reData1 = list(reversed(temp1))
            reData2 = list(reversed(temp2))

            # 회문인지 검사
            if temp1 == reData1:
                count += 1
            if temp2 == reData2:
                count += 1

    # 결과 출력
    print(f"#{tc} {count}")

### 1215. [S/W 문제해결 기본] 3일차 - 회문1