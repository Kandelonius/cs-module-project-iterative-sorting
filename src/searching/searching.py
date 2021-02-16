def linear_search(arr, target):
    for elem in arr:
        # print(f"value is {arr[elem]}")
        if target == elem:
            return arr.index(elem)
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    min = 0
    max = len(arr) - 1
    while min <= max:
        midpoint = (max + min) // 2
        if target == arr[midpoint]:
            return midpoint
        elif target < arr[midpoint]:
            max = midpoint - 1
        else:
            min = midpoint + 1
    return -1  # not found

# arr1 = [-2, 2, 2, 7, 7, 7, 7, 7, 7]
# arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]

# print(linear_search(arr1, -6))