# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 02:04:54 2022

@author: Avinash Kumar
"""

def getMaxLen(nums):
        if len(nums) == 0 :
            return 0
        elif len(nums) == 1:
            if nums[0] >= 0:
                return 1
            else:
                return 0
            
        res = 0
        pos = 0
        neg = 0
        for num in nums:
            if num > 0:
                pos = pos + 1 if pos > 0 else 1
                neg = neg + 1 if neg > 0 else 0
            elif num < 0:
                pp, nn = pos, neg
                pos = nn + 1 if nn > 0 else 0
                neg = pp + 1 if pp > 0 else 1
            else:
                pos = neg = 0
            res = max(res, pos)
        return res
    
nums = [-1,-2,-3,0,1]
res = getMaxLen(nums)
print(res)