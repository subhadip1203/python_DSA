import heapq

arr = [5, 7, 9, 2, 3]

heapq.heapify(arr)
print (list(arr))

heapq.heappush(arr,4)
heapq.heappush(arr,1)
print (list(arr))

heapq.heappop(arr)
print (list(arr))


# heap for tuples , only first elemnt will be considered
# tuple index zero [0] , will be consider for assending order

arr2 = []
heapq.heapify(arr2)

heapq.heappush(arr2,(10,25))
print (list(arr2))

heapq.heappush(arr2,(1,25))
print (list(arr2))

heapq.heappush(arr2,(10,20))
print (list(arr2))

heapq.heappush(arr2,(9,20))
print (list(arr2))