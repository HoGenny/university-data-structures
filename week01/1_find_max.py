Data = [3,2,5,4,1]
max = Data[0]
wheremax = -1

for now in range(len(Data)):
    if Data[now] > max:
        max = Data[now]
        wheremax = now

print(max, wheremax)