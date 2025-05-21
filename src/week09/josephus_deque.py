from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

# 전체 인원 수(howMany)와 제거할 순서(K) 입력
howMany, K = map(int, input().split())

# 1번부터 howMany번까지 deque 초기화
Queue = deque(range(1, howMany + 1))

# 출력 시작 포맷
print('<', end='')

# 큐에 한 명 남을 때까지 반복
while len(Queue) > 1:
    # 앞에서 K-1명은 뒤로 보내기
    for _ in range(K - 1):
        Queue.append(Queue.popleft())

    # K번째 사람 제거 및 출력
    print(Queue.popleft(), end=', ')

# 마지막 한 명 출력 (쉼표 없이)
print(Queue.popleft(), end='')

# 출력 마무리
print('>')