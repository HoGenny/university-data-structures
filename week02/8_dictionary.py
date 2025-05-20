lunch = {}

for _ in range(2):
    menu, price = input("메뉴가격입력").split()
    lunch[menu] = price

print(lunch)
# what = input("원하는 메뉴")
# print(lunch[what])