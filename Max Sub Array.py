# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 20:31:36 2022

@author: Avinash Kumar
"""

def maxSubArray(nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        currSum = nums[0]
        maxSum = nums[0]
        
        for i in range(1, len(nums)):
            currSum = max(nums[i], nums[i]+ currSum)
            maxSum = max(currSum, maxSum)
        return maxSum
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
res = maxSubArray(nums)
print(res)