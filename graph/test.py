# path=[["123","456"],["789","101112"]]
# start="abc"
# path = path + [start]
# path.append(start)
# print(path)



def change_array(arr):
    # arr.append("abc")
    arr=arr+["abc"]
    print(arr)

path=["123","456","789"]
change_array(path)
print(path)