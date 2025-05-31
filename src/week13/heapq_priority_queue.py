import sys
sys.stdin = open("input.txt", 'r')

def insert_into_minQueue(pQueue, value):
    pQueue.append(value)
    where = len(pQueue) - 1
    while where > 1 and pQueue[where] < pQueue[where >> 1]:
        pQueue[where], pQueue[where >> 1] = pQueue[where >> 1], pQueue[where]
        where >>= 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    pQueue = [0]

    for value in data:
        insert_into_minQueue(pQueue, value)
    where = len(pQueue) - 1
    total = 0
    while where > 1:
        where >>= 1
        total += pQueue[where]
    print(f'#{tc} {total}')

### SWEA 5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙