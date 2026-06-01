# Selection Sort repeatedly selects the smallest element from the unsorted portion and places it in its correct position.
def selection_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        smallest_idx = i
        for j in range(i+1, len(nums)):
            smallest_idx = j
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]

    return nums

## Big o notation
# O (n^2) in every case 

## Space complexity
# O(1) sorts in place using only a few extra variables (i,j,smallest_idx)
