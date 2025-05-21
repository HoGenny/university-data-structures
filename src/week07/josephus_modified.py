# 큐 초기화
queue = []

# 총 사람 수
people = 41

# 1번부터 41번까지 사람을 큐에 삽입
for who in range(1, people + 1):
    queue.append(who)

# 큐에 3명만 남을 때까지 반복
while len(queue) != 3:
    alive1 = queue.pop(0)  # 첫 번째 사람 생존
    alive2 = queue.pop(0)  # 두 번째 사람 생존
    dead = queue.pop(0)    # 세 번째 사람 제거

    # 생존자는 다시 큐 뒤로 추가
    queue.append(alive1)
    queue.append(alive2)

# 마지막에 남은 두 사람 출력
print(queue.pop(0), queue.pop(0))

### 이 코드는 3명씩 묶어 2명 생존, 1명 제거를 반복하여 최종적으로 2명만 남을 때까지 실행됩니다. (요세푸스 문제)