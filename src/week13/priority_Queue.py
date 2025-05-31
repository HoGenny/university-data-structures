import heapq

q = []
heapq.heappush(q, 3)
heapq.heappush(q, 10)
heapq.heappush(q, 1)
heapq.heappush(q, 0)
heapq.heappush(q, 4)

print(q)  # [0, 1, 3, 10, 4]
print(heapq.heappop(q))
print(q)  # [1, 4, 3, 10]

q2 = [9, 20, 1, 8, 5, 0]

heapq.heapify(q2)
print(q2)  # [0, 5, 1, 8, 20, 9]

# q에서 가장 큰 3개의 원소가 담긴 리스트
print(heapq.nlargest(n=3, iterable=q))  # [10, 4, 3]

# q에서 가장 작은 3개의 원소가 담긴 리스트
print(heapq.nsmallest(n=3, iterable=q))  # [0, 1, 3]