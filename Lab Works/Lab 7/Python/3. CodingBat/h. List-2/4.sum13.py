def sum13(nums):
    if not nums:
        return 0

    sum = 0
    skip_next = False
    for i in range(len(nums)):
        if nums[i] == 13:
            skip_next = True
        elif not skip_next:
            sum += nums[i]
        else:
            skip_next = False

    return sum
