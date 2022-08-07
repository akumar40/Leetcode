# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 14:24:22 2022

@author: Avinash Kumar
"""
from itertools import combinations

def subArrayRanges(nums):
        if len(nums) <= 1:
            return 0
        sum = 0
        for i in range(len(nums)):
            l,r = nums[i], nums[i]
            for j in range(i, len(nums)):
                l = min(l, nums[j])
                r = max(r, nums[j])
                sum+= r - l
        return sum
    
nums = [1,2,3]
res = subArrayRanges(nums)
print(res)