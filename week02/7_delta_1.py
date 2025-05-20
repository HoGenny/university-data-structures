data = [[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

whereY = -1
whereX = -1

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 11:
            whereY = y
            whereX = x

for dir in range(4):
    newY = whereY + dy[dir]
    newX = whereX + dx[dir]

    if 0 <= newY < 5 and 0 <= newX < 5:
        print(data[newY][newX])