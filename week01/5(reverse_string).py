Data = [i for i in range(1,7)]
start, end = 3, 5
dummy = Data[3:6]

dummy.reverse()
Data[start:end+1] = dummy
print(Data)