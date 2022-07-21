# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:00:34 2022

@author: Avinash Kumar
"""

class MovingAverage:
    size = 0
    lst = []
    
    def __init__(self, size: int):
        self.size = size
        
    def next(self, val:int) -> float:
        if len(self.lst) < self.size:
            self.lst.append(val)
            return float(sum(self.lst)/len(self.lst))
        else:
            self.lst.pop(0)
            self.lst.append(val)
            return float(sum(self.lst)/len(self.lst))

obj = MovingAverage(1)
print(obj.next(-1))
