# merge sort is an recursive sorting algorithm (calls itself until the list is not divided) 
# its a divide(divide larger problems into smaller ones and recursively solve it) and conquer(combine the result of the smaller problems to solve the larger problems) algorithm

# we divide list into two halves recursively sort on the two halves merge the two halves to form a sorted array
def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums

    middle = len(nums) // 2
    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])

    return merge(left, right) 

def merge(first: list[int], second: list[int]) -> list[int]:
    pass
