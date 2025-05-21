# 정렬할 데이터
data = [9, 6, 8, 3, 1, 7, 5, 2, 4]

# 셸 정렬 함수 정의
def Shell_sort():
    howmany = len(data)
    howfar = howmany >> 1  # 초기 gap 설정 (리스트 길이의 절반)

    # gap이 0보다 클 때까지 반복
    while howfar > 0:
        # gap 간격을 두고 삽입 정렬 수행
        for now in range(howfar, howmany):
            temp = data[now]
            where = now
            compareWhere = where - howfar

            # gap 간격으로 이전 값들과 비교해 삽입 정렬 수행
            while compareWhere >= 0:
                if data[compareWhere] > temp:
                    data[where] = data[compareWhere]
                    where -= howfar
                    compareWhere -= howfar
                else:
                    break
            data[where] = temp

        # gap 반으로 줄이기
        howfar >>= 1

# 셸 정렬 실행
Shell_sort()

# 결과 출력
print(data)