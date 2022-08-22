# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 22:17:49 2022

@author: Avinash Kumar
"""

def canAttendMeetings(intervals):
        intervals.sort(key= lambda x : x[0])
        return all(j[0] >= i[1] for i,j in zip(intervals, intervals[1:]))
    
intervals = [[0,30],[5,10],[15,20]]
res = canAttendMeetings(intervals)
print(res)