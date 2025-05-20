data = [0,4,1,3,1,2,4,1]
iamMax = max(data)

count = [0] * (iamMax + 1)

# for i in range(len(data)):
#     count[data[i]] += 1
for now in data:
    count[now] += 1
    
for i in range(1, len(count)):
    count[i] += count[i-1]

result = [0] * len(data)
for now in data[::-1]:
    count[now] -= 1
    result[count[now]] = now

print(result)