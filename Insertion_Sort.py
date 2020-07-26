def insertion_sort(lst):
    for i in range(1,len(lst)):
        val_to_sort = lst[i]
        while lst[i-1] > val_to_sort and i > 0:
            lst[i-1],lst[i] = lst[i],lst[i-1]
            i-=1
    return lst
print(insertion_sort([9,8,7,6,5,4,3,2,1]))
