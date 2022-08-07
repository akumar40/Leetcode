# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 23:10:28 2022

@author: Avinash Kumar
"""

def appealSum(s: str):
        last = {}
        cur = 0
        res = 0
        for i, ch in enumerate(s):
            cur += i - (last[ch] if ch in last else -1)
            last[ch] = i
            res += cur
        return res
    
s = "aba"
res = appealSum(s)
print(res)