# 리스트를 이용한 간단한 큐 구현
Queue = []

# 1부터 3까지 큐에 삽입 (enqueue)
for i in range(1, 4):
    Queue.append(i)  # 큐에 넣기

# 큐가 빌 때까지 앞에서부터 꺼내기 (dequeue)
while Queue:
    print(Queue.pop(0))  # 큐의 맨 앞 요소 출력 및 제거