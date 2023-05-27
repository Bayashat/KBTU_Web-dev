def no_teen_sum(a, b, c):
  nums = [a,b,c]
  for i in range(len(nums)):
    if nums[i] == 15 or nums[i] == 16:
      continue
    if 13 <= nums[i] <= 19:
      nums[i] = fix_teen(nums[i])
  return sum(nums)
      
def fix_teen(n):
  return 0