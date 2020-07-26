def selection_sort(lst):
    n = len(lst)-1
    for i in range(n):
        mini_value = i
        for j in range(i+1,n+1):
            if lst[j] < lst[mini_value]:
                mini_value = j
        if mini_value !=i:
            lst[mini_value],lst[i] = lst[i],lst[mini_value]
    return lst
print(selection_sort([9,8,7,6,5,4,3,2,1]))
