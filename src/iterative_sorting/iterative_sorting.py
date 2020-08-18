import random


def selection_sort(arr):
    # loop through n-1 elements
    for outer in range(0, len(arr) - 1): # range 0 - length - 1 so we don't go out of range in inner loop
        cur_index = outer  # set iterating index
        # (hint, can do in 3 loc)
        ## set the first index as minimum
        smallest_index = cur_index  # set index of the smallest element
        ## compare minimum with the next element and if that is smaller reset minimum
        for inner in range(outer + 1, len(arr)):  # loop through the array starting with the current index
            if arr[inner] < arr[
                smallest_index]:  # check if the item at the inner arrays current is smaller than the previous smallest
                smallest_index = inner  # set smallest index to the new smaller index
            ## then continue to the end of the array checking each element.
            ## if none are smaller, swap smallest with current then continue until all elements are sorted.
        temp = arr[outer]  # store leftmost value
        arr[outer] = arr[smallest_index]  # set leftmost value to smallest value
        arr[smallest_index] = temp
        # (arr[outer], arr[smallest_index]) = (
        #     arr[cur_index], arr[outer])  # using stored indexes and values to make the swap
    # print(arr)
    return arr


def bubble_sort(arr):
    """
    start at the first index and compare the first and second items
    if the second item is smaller, swap them and evaluate second and third the same way
    """
    for outer in range(len(arr)): # times looping through the full array
        for inner in range(0, len(arr) - outer - 1): # loop through the remaining elements
            # checking if left is larger than right
            if arr[inner] > arr[inner + 1]:
                # then swapping if it is
                temp = arr[inner + 1] # storing the value of the earlier element
                arr[inner + 1] = arr[inner]
                arr[inner] = temp
    print(arr)
    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # find the max element as this is required knowledge for count sort
    # initialize an array of max + 1 and fill it with 0
    max = 0
    size = len(arr)
    output = [0] * size
    for elem in arr:
        if elem > max:
            max = elem
    temp_arr = [0] * (max + 1)
    # for place in range(maximum + 1):
    #     temparr[place] = 0
    # store the count of each element at their respective index in temp array
    # ie how many times does this value appear
    for value in range(0, size):
        temp_arr[arr[value]] += 1

    # find the index of each element of the original array in the count array
    for index in range(1, max + 1):
        temp_arr[index] += temp_arr[index - 1]

    iterations = size - 1
    while iterations >= 0:
        output[temp_arr[arr[iterations]] - 1] = arr[iterations]
        temp_arr[arr[iterations]] -= 1
        iterations -= 1

    for i in range(0, size):
        arr[i] = temp_arr[i]
    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# (selection_sort(arr1))

bubble_sort(arr1)
# arr4 = random.sample(range(200), 50)
#
# (selection_sort(arr4), sorted(arr4))
