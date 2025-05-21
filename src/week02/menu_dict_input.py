# 빈 딕셔너리 생성 (메뉴:가격 저장용)
lunch = {}

# 2개의 메뉴와 가격을 입력받아 딕셔너리에 저장
for _ in range(2):
    menu, price = input("메뉴가격입력: ").split()
    lunch[menu] = price  # 키: 메뉴, 값: 가격

# 전체 딕셔너리 출력
print(lunch)

# 아래는 특정 메뉴의 가격을 조회하는 코드
# what = input("원하는 메뉴: ")
# print(lunch[what])