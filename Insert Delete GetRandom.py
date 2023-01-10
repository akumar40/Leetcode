# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:12:48 2023

@author: Avinash Kumar
"""
import random

class RandomizedSet:

    def __init__(self):
        self.elem = set()
        self.size = 0

    def insert(self, val: int) -> bool:
        o_size = self.size
        self.elem.add(val)
        n_size = len(self.elem)
        if o_size != n_size:
            self.size = n_size
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.elem:
            self.elem.remove(val)
            self.size -= 1
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(list(self.elem))
    
# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.insert(2))
print(obj.getRandom())