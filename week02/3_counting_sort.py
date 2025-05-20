data = [0,4,1,3,1,2,4,1]
iamMax = max(data)

count = [0] * (iamMax + 1)

# for i in range(len(data)):
#     count[data[i]] += 1
for now in data:
    count[now] += 1
    
print(count)