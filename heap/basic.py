import heapq

arr = [5, 7, 9, 2, 3]

heapq.heapify(arr)
print (list(arr))

heapq.heappush(arr,4)
heapq.heappush(arr,1)
print (list(arr))

heapq.heappop(arr)
print (list(arr))