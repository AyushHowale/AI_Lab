def selection_sort_simple(arr):
    sorted_arr = []
    
    while arr:
        # Find the minimum element in the original array
        min_val = min(arr)
        sorted_arr.append(min_val)      # Add it to the sorted array
        arr.remove(min_val)             # Remove it from the original array

    return sorted_arr

# Example
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort_simple(arr)
print("Sorted array:", sorted_arr)
