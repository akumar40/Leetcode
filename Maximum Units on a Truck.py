# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 17:35:01 2022

@author: Avinash Kumar
"""

def maximumUnits(boxTypes, truckSize):
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        units = 0
        for boxes, unit in boxTypes:
            if truckSize >= boxes:
                units += boxes * unit
                truckSize-= boxes
            else:
                units += truckSize * unit
                truckSize = 0
                break
        return units
    
boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
res = maximumUnits(boxTypes, truckSize)
print(res)