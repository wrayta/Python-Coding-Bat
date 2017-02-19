"""
Given an array length 1 or more of ints, return the difference between the 
largest and smallest values in the array. Note: the built-in min(v1, v2) and
max(v1, v2) functions return the smaller or larger of two values.

big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
"""
def big_diff(nums):
  maxNum = nums[0]
  currentMax = nums[0]
  
  minNum = nums[0]
  currentMin = nums[0]
  
  i = 0
  
  while i < len(nums):
    if i + 1 < len(nums):
      currentMin = min(nums[i], nums[i + 1])
      
      if currentMin < minNum:
        minNum = currentMin
      
      currentMax = max(nums[i], nums[i + 1])
      
      if currentMax > maxNum:
        maxNum = currentMax
      
    i += 1
  
  return maxNum - minNum
