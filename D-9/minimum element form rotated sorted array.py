def find_min(nums):
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return nums[low]


nums = [5,6,7,0,1,2,3]
print("Minimum element is:", find_min(nums))
