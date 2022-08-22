# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 21:36:08 2022

@author: Avinash Kumar
"""

def canFinish(numCourses, prerequisites):
        graph = [[] for x in range(numCourses)]
        for a,b in prerequisites:
            graph[a].append(b)
            
        visit = [0 for x in range(numCourses)]
        for i in range(numCourses):
            if not dfs(i, graph, visit):
                return False
        return True
            
    
def dfs(i, graph, visit):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j, graph, visit):
                return False
        visit[i] = 1
        return True
    
numCourses = 2
prerequisites = [[1,0]]
result = canFinish(numCourses, prerequisites)
print(result)