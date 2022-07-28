# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:18:27 2022

@author: Avinash Kumar
"""

def kClosest(points, k: int):
    rec = {}
    res = []
    for idx, point in enumerate(points):
        rec[idx] = euclD(point[0], point[1])
    
    rec = sorted(rec.items(), key=lambda item:item[1])
    for dist in rec:
        if len(res) < k:
            res.append(points[dist[0]])
        else:
            break
    return res
        
        
        
def euclD(pointA, pointB):
    return (pointA * pointA) + (pointB * pointB)


points = [[3,3],[5,-1],[-2,4]]
k = 2
res = kClosest(points, k)
print(res)