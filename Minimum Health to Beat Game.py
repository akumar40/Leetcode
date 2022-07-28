# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 14:05:43 2022

@author: Avinash Kumar
"""

def minimumHealth(damage: [], armor: int) -> int:
    if armor == 0:
        return sum(damage) + 1
    idx = -1
    if armor in damage:
        idx = damage.index(armor)
        return calHealth(damage, idx) + 1
    else:
        maxVal = max(damage)
        idx = damage.index(maxVal)
        return calHealth(damage, idx) + (1 if maxVal < armor else (maxVal - armor + 1))
        
        
def calHealth(damage: [], idx: int):
    minHealth = 0
    for i, dam in enumerate(damage):
        if i == idx:
            continue
        minHealth += damage[i]
    return minHealth
    
    
damage = [3,3,3]
armor = 0
res = minimumHealth(damage, armor)
print(res)