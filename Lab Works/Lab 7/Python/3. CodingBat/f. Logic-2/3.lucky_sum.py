def lucky_sum(a, b, c):
    nums = [a, b, c]
    if 13 in nums:
        return sum(nums[:nums.index(13)])
    else:
        return sum(nums)
