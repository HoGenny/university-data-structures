# 시작 숫자 초기화
num = 0

# 5행 반복
for y in range(5):
    # 각 행마다 5열 반복
    for x in range(5):
        num += 1                     # 숫자 1씩 증가
        print(num, end=' ')          # 줄바꿈 없이 출력
    print()                          # 행이 끝나면 줄바꿈

### 이 코드는 5x5 격자 형태로 1부터 25까지 출력하는 중첩 반복문입니다.