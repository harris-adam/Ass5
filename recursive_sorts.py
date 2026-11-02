# recursive_sorts.py
# merge sort, quicksort, hybrid sort
# Strongly suggest you turn off LLMs like
# GitHub Copilot, TabNine, etc. when working on this file.
# Writing a sorting algorithm yourself is the best
# way to learn how it works.
# Modified by: Harris Adam
from random import randint


# This function assumes both left and right are sorted
# lists, each in ascending order
# This is already done, don't modify it
def merge(left, right):
    # pre-allocate memory for the merged lists
    merged = [None] * (len(left) + len(right))
    left_index = 0
    right_index = 0
    merged_index = 0
    # move the smallest element from left or right to merged
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged[merged_index] = left[left_index]
            left_index += 1
        else:
            merged[merged_index] = right[right_index]
            right_index += 1
        merged_index += 1
    # copy any remaining elements from left
    while left_index < len(left):
        merged[merged_index] = left[left_index]
        left_index += 1
        merged_index += 1
    # copy any remaining elements from right
    while right_index < len(right):
        merged[merged_index] = right[right_index]
        right_index += 1
        merged_index += 1
    return merged


# Sort a list in ascending order using the
# merge sort algorithm including the provided
# merge function above
# lst[:] = ...
# will replace all the elements in the list with 
# whatever is on the right side of the = sign
# Don't return anything, just replace the elements
# in lst with the sorted elements
def merge_sort(lst):
    # Base case: a list of 0 or 1 items is already sorted
    if len(lst) <= 1:
        return
    # Split the list into two halves (copies)
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    # Recursively sort each half
    merge_sort(left)
    merge_sort(right)
    # Merge the two sorted halves and replace the contents of lst
    lst[:] = merge(left, right)


# Sorts a list in ascending order using the quicksort algorithm
# between *start* and *end* inclusive
# Meaning if we had a list like [5, 3, 8, 6, 2]
# and we called quicksort_in_place(lst, 1, 3)
# it would result in the list [5, 3, 6, 8, 2]
# Please choose a random pivot index between
# start and end inclusive using randint
# Don't return anything, just sort lst in-place
def quicksort_in_place(lst, start, end):
    # Base case: a range with 0 or 1 items is already sorted
    if start >= end:
        return
    # Choose a random pivot index between start and end inclusive
    pivot_index = randint(start, end)
    pivot = lst[pivot_index]
    # Move the pivot to the end of the range
    lst[pivot_index], lst[end] = lst[end], lst[pivot_index]
    # Partition: store_index marks where the next "less than pivot"
    # item belongs; everything before it is less than the pivot
    store_index = start
    for i in range(start, end):
        if lst[i] < pivot:
            lst[i], lst[store_index] = lst[store_index], lst[i]
            store_index += 1
    # Move the pivot between the "less than" and "greater or equal" sides
    lst[store_index], lst[end] = lst[end], lst[store_index]
    # Recursively sort each side (the pivot is already in its final place)
    quicksort_in_place(lst, start, store_index - 1)
    quicksort_in_place(lst, store_index + 1, end)


# This is already done, don't modify it
def quicksort(lst):
    quicksort_in_place(lst, 0, len(lst) - 1)


# This is already done, don't modify it
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


# Perform a hybrid sort using the merge sort algorithm
# (although not the merge sort function) for lists
# larger than threshold, and insertion sort for lists
# smaller than or equal to threshold
# Sort in ascending order
# See the note about [:] above merge_sort()
# Don't return anything, just sort lst's items and replace them
def hybrid_sort(lst, threshold=10):
    # Base case: small lists are faster to sort with insertion sort
    if len(lst) <= threshold:
        insertion_sort(lst)
        return
    # Otherwise do merge sort: split into two halves (copies)
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    # Recursively sort each half with the hybrid sort
    hybrid_sort(left, threshold)
    hybrid_sort(right, threshold)
    # Merge the sorted halves and replace the contents of lst
    lst[:] = merge(left, right)
