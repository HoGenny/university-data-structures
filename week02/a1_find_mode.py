import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    dummy = int(input())
    data = list(map(int, input().split()))
    count = [0] * 101
    
    for now in data:
        count[now] += 1
    max = count[0]
    wheremax = -1
    
    for now in range(len(count)):
        if max <= count[now]:
            max = count[now]
            wheremax = now
    print(f"#{tc} {wheremax}")