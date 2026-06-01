# bubble_sort.
# compare i-1 elemnt to i and swap if needed.
# continue mkaing passes until a pass completes with no swaps.
# after each pass, the largest unsorted element is places at the end.

def bubble_sort(nums: list[int]) -> list[int]:
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        end = len(nums)
        for i in range(1,end):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swapping = True
        end -= 1 
    return nums

## u can test this algorithm from below code snippet.

#arr = [1,4,8,9,2,5,4,6]
#result = bubble_sort(arr)
#print(result)


## 1. Big O complexity
# worst case (O^2)
# for every element we need to compare it with almost every other element
# so for 5 elements 1st pass has 4 comparision, then 2nd pass hai 3 comparision, then 3rd pass has 2 and 4th pass has 1.
# for n elements (n-1) * (n-2) * (n-3) * (n-4) .... * 1 
# it grows roughly like n(n-1)/n-2
# which becomes O^n-2

# best case (O(n))
# comaprision n-1
# so o(n)

# avg case (O^2) because most random list are nrither full sorted nor fully reversed.


## 2. Space complexity
# u only use few variables no extra list is created so its (O(1))

## bubble sort has nested behaviour so the list is scanned again and again so the repeated work is n*n so n^2

 
