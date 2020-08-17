import random


def selection_sort(arr):
    # loop through n-1 elements
    for outer in range(0, len(arr) - 1):
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

        # TO-DO: swap
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
    # Your code here

    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# (selection_sort(arr1))

bubble_sort(arr1)
# arr4 = random.sample(range(200), 50)
#
# (selection_sort(arr4), sorted(arr4))
