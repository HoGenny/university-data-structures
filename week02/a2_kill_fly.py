import sys
sys.stdin = open('input.txt', 'r')

def isSafe(y, x, N):
    return 0 <= x < N and 0 <= y < N

for tc in range(int(input())):
    N, M = map(int, input().split())

    myMap = [list(map(int, input().split())) for _ in range(N)]
    result = 0
        
    dy1 = [-1, 0, 1, 0]
    dx1 = [0, 1, 0, -1]

    for y in range(N):
        for x in range(N):
            sum = myMap[y][x]
            for dir in range(4):
                for size in range(1, M):
                    newY, newX = y + dy1[dir] * size, x + dx1[dir] * size
                    if isSafe(newY, newX, N):
                        sum += myMap[newY][newX]
                if sum > result:
                    result = sum

    dy2 = [1,1,-1,-1]
    dx2 = [-1,1,-1,1]

    for y in range(N):
        for x in range(N):
            sum = myMap[y][x]
            for dir in range(4):
                for size in range(1, M):
                    newY, newX = y + dy2[dir] * size, x + dx2[dir] * size
                    if isSafe(newY, newX, N):
                        sum += myMap[newY][newX]
                if sum > result:
                    result = sum
    print(f'#{tc+1} {result}')