# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 12:40:36 2023

@author: Avinash Kumar
"""

def twoCitySchedCost(costs) -> int:
    cityA = sum([i for i,j in costs])
    cityB = [j-i for i,j in costs]
    cityB.sort()
    cityB = sum(cityB[:len(costs)//2])
    return cityA + cityB

costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
result = twoCitySchedCost(costs)
print(result)

# def twoCitySchedCost(self, costs: List[List[int]]) -> int:
#         costs.sort(key= lambda x:x[1] - x[0])

#         num = len(costs) // 2
#         res = 0
#         for i in range(num):
#             res += costs[i][1]
#             res += costs[i+num][0]
#         return res