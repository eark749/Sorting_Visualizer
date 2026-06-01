# Quick Sort is an efficient sorting algorithm that's widely used in production sorting implementation. it is same like merge sort recursive divide and conquer algorithm
# we have a list. we choose a pivot (eg:- the last element). then we rearrange the array so that all elements smaller than the pivot are on the left and all the higher elements on the right. after partitioning, the pivot is in its correct final postion. then we recursivly apply this to left and right subarrays. we keep doing until the sub array has 0 or 1 element left, because with 0 and 1 elements are already sorted.


def quick_sort(nums: list[int], low: int, high:int) -> None:
    if low < high:
        middle = partition(nums,low,high)
        quick_sort(nums, low, middle-1)
        quick_sort(nums, middle+1, high)

def partition(nums: list[int], low: int, high: int) -> int:
    pivot = nums[high]
    i = low -1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1 
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i+1 

##test it out
#nums = [7, 2, 1, 8, 6, 3, 5, 4]
#print("Before:", nums)
#quick_sort(nums, 0, len(nums) - 1)
#print("After: ", nums)


## Big O notation
# worst time complexity O(n^2) pivot is always the highest or the smallest creating highly unbalanced partitions
# best and svg is O(n logn) pivots splits the array half each time

## Space complexity
# best case O (logn) because of recursion ca=ll stack depth
# worst case O(n) recursion tree becomes straight line


## there are ways to fix the quick sort function
# two approaches
# 1. random approch:- the function simply shuffles the list before sorting
# 2. median approach:- use the middle value as pivot to reduce the chance of unbalanced partions and import partition


