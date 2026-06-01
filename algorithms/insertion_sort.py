# Insertion Sort:- for each element starting from index 1 to range len(arr) we set j to current index (which is i) then while j is > 0 and current element is smaller than hte preious element then swap and decrement j till the element is in the correct position. is already in correct position then move to the next index

def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(1,len(nums)):                                  
        j = i                                         # we set the j to the current variable
        while j>0 and nums[j] < nums[j-1]:            # while j > 0 and if i is smaller than j-1 swap it 
            nums[j], nums[j-1] = nums[j-1], nums[j]   # swapping
            j -= 1                                    # we decrement j with 1 
    return nums

## use this to test the fucntion
# arr = [5, 3, 8, 1]
# print(insertion_sort(arr))


## Big O notation 
# worst case is O(n^2) because every element moves all the way to beginnning
# avg case also O(n^2) 
# best case O(n) array is already sorted, so each element is already sorted so elements qare checked only once. 

## Space complexity
# O(1) constant because we only use variable not memory here we do it in place thats why



