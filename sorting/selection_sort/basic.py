
def selection_sort(seq):
    size= len(seq)
    for i in range(size-1):
        min_index = i
        for j in range (min_index+1, size):
            if seq[j] < seq[min_index]:
                min_index = j
        if i != min_index:
            seq[i],seq[min_index] = seq[min_index],seq[i]
    return seq

x=[10,9,1,2,4,5,6,7,4]
print(selection_sort(x))