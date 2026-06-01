# merge sort is an recursive sorting algorithm (calls itself until the list is not divided) 
# its a divide(divide larger problems into smaller ones and recursively solve it) and conquer(combine the result of the smaller problems to solve the larger problems) algorithm

# we divide list into two halves recursively sort on the two halves merge the two halves to form a sorted array

def merge_sort(nums: list[int]) -> list[int]: #keep splitting the list into smaller and smaller pieces until each piece has 0 or 1 element.
    if len(nums) < 2:
        return nums

    middle = len(nums) // 2
    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])

    return merge(left, right) 

def merge(first: list[int], second: list[int]) -> list[int]:
    final = []
    i = j = 0
    while i < len(first) and j < len(second):  # Main loop: compare elements from BOTH LISTS
        if first[i] < second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):                       # left over loop: copy whatever remains after one lists runs out 
        final.append(first[i])
        i += 1
    while j < len(second):                      # left over loop: copy whatever remains after one lists runs out
        final.append(second[j])       
        j += 1
    return final

## use this to test the function 
#arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#result = merge_sort(arr)
#print(result)


## Big O notation
# worst case, best case, avg case all of them are O(n * log n) = O(nlogn). this is beacuse there is log2(n) levels of splitting and each merge level processes all n elements once, giving O(n) times, giving O(nlogn).

## space complexity
# merge sort uses O(n) because it creates temp arrays while splitting and merging, but the maximum additional memroy required at any point is proportional to the size of the input array.


## when to use
# when you need a fast sorting algorithm and memeory isnt the issue


