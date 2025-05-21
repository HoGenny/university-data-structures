# 시작할 두 숫자 중 두 번째 숫자
num = 62

# 시퀀스를 저장할 리스트 초기화
MyList = []

# 첫 번째와 두 번째 값을 리스트에 추가
MyList.append(100)
MyList.append(num)

# 이전 두 수의 차를 계산해 다음 수로 추가하며 음수가 나올 때까지 반복
while True:
    MyList.append(MyList[-2] - MyList[-1])  # 앞의 두 수 차이 추가
    if MyList[-1] < 0:  # 마지막 값이 음수면 종료
        break

# 결과 출력 (한 줄로)
for now in MyList:
    print(now, end=' ')

### 처음 두 수를 기준으로 시작해, 매번 앞의 두 수의 차를 다음 항으로 추가하는 수열입니다.
### 일종의 특이한 피보나치 반대 버전이라 볼 수 있습니다.