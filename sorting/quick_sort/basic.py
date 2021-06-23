def quick_sort(seq):
    length = len(seq)
    if length <= 1:
        return seq
    else:
        pivot = seq.pop()
    
    items_greater = []
    items_lesser= []
    for itm in seq:
        if itm< pivot:
            items_lesser.append(itm)
        else:
            items_greater.append(itm)

    return quick_sort(items_lesser)+[pivot]+quick_sort(items_greater)


my_arr=[10,9,1,4,2,7,4,5]
print(quick_sort(my_arr))