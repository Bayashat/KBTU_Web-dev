def centered_average(nums):
    nums.sort()  # Sort the array in ascending order
    nums = nums[1:-1]  # Ignore the first and last elements
    return sum(nums) // len(nums)  # Return the integer division of the sum and length of the array
