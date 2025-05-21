# 빈 스택 생성
stack = []

# 1부터 3까지 스택에 push (append)
for i in range(1, 4):
    stack.append(i)  # 스택에 값 추가: [1, 2, 3]

# 스택이 비어있지 않을 동안 pop하여 출력
while stack:
    print(stack.pop())  # 후입선출(LIFO)에 따라 3, 2, 1 순으로 출력