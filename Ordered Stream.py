# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 08:22:13 2023

@author: Avinash Kumar
"""

class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n
        self.ptr = 0        

    def insert(self, idKey: int, value: str):
        idKey-=1
        self.stream[idKey] = value
        res = []
        
        while self.ptr < len(self.stream) and self.stream[self.ptr]:
            res.append(self.stream[self.ptr])
            self.ptr += 1
        
        return res
    
# Your OrderedStream object will be instantiated and called as such:
obj = OrderedStream(5)
print(obj.insert(3,"ccccc"))
print(obj.insert(1,"aaaaa"))
print(obj.insert(2,"bbbbb"))
print(obj.insert(5,"eeeee"))
print(obj.insert(4,"ddddd"))