# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 02:24:00 2022

@author: Avinash Kumar
"""

def getFood( grid):
        n = len(grid[0])
        for i in range(len(grid)):
            for j in range(n):
                if grid[i][j] == '*':
                    count = search(grid, i, j, [], 0)
                    return count if count is not None and count > 0 else -1
        return -1
                    
def search(grid, i, j,visited, step):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 'X' or isVisited(visited, i, j):
            return None
        
        visited.append([i,j])
        
        if grid[i][j] == '#':
            return step
        
        temp = visited
        
        steps = [search(grid, i + 1, j,temp, step + 1), search(grid, i - 1, j,temp, step + 1), search(grid, i, j + 1,temp, step + 1), search(grid, i, j - 1,temp, step + 1)]
        
        steps = [step for step in steps if step is not None]
        if len(steps) <= 0:
            return 0
        return min(steps)
    
def isVisited(visited, i, j):
        for a,b in visited:
            if a == i and b == j:
                return True
        return False
    
grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
res = getFood(grid)
print(res)