def selection_sort_simple(arr):
    sorted_arr = []
    
    while arr:
       
        min_val = min(arr)
        sorted_arr.append(min_val)      
        arr.remove(min_val)             

    return sorted_arr


arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort_simple(arr)
print("Sorted array:", sorted_arr)
