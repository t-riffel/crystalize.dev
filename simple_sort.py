def partition(left, right, values):
    # start at the ends
    pivot, ptr = values[right], left
    for i in range(left, right):
        if values[i] <= pivot:
            # swap smaller to the front
            values[i], values[ptr] = values[ptr], values[i]
            ptr += 1
    # swap end with ptr value
    values[ptr], values[right] = values[right], values[ptr]
    return ptr
 
def quicksort(left, right, values):
    # recursion end case is 1 value in array
    if len(values) == 1:
        return values
    if left < right:
        pivot = partition(left, right, values)
        quicksort(left, pivot - 1, values)
        quicksort(pivot + 1, right, values)
    return values
  
  array = [10, 2, 3, 5, 7, 9]
  
  print(quicksort(0, len(array) - 1, 2))
