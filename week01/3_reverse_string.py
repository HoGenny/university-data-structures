Data = [i for i in range(1,7)]
howmany = len(Data)

for i in range(howmany//2):
    Data[i], Data[howmany-1-i] = Data[howmany-1-i], Data[i]
print(Data)

Data.reverse()
print(Data)

print(Data[::-1])