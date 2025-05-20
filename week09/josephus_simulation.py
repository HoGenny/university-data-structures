import sys
sys.stdin = open('input.txt', 'r')

# 총 인원 수(howMany), 제거할 순서(K) 입력
howMany, K = map(int, input().split())

# 1번부터 howMany번까지 번호를 큐에 초기화
Queue = list(range(1, howMany + 1))

# 출력 시작
print('<', end='')

# 큐에 1명 남을 때까지 반복
while len(Queue) > 1:
    # K-1번 앞 사람을 뒤로 보내면서 순서를 맞춤
    for _ in range(K - 1):
        Queue.append(Queue.pop(0))  # 맨 앞을 뒤로 보냄

    # K번째 사람을 제거 및 출력
    print(Queue.pop(0), end=', ')

# 마지막 남은 사람 출력 (마지막엔 쉼표 없이)
print(Queue.pop(0), end='')

# 출력 마무리
print('>')
