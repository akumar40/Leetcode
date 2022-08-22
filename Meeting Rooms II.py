# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 01:21:53 2022

@author: Avinash Kumar
"""

import heapq

def minMeetingRooms(intervals):
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1
        heap = []
        intervals.sort(key=lambda x: x[0])
        for x, y in intervals:
            if not heap or heap[0] > x:
                # rooms are still in use
                heapq.heappush(heap, y)
            else: # free room available , replace with current meeting 
                heapq.heappushpop(heap,y)

        return len(heap)
    
intervals = [[0,30],[5,10],[15,20]]
res = minMeetingRooms(intervals)
print(res)