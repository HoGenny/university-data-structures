data = [2,4,7,9,11,19,23]
key = 9

start = 0
end = len(data)-1

while start<=end:
    mid = (start + end) // 2
    if data[mid]==key:
        print("찾았다")
        break
    elif data[mid]>key:
        end = mid-1
    else:
        start = mid+1
