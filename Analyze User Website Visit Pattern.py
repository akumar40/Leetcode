# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 22:55:39 2022

@author: Avinash Kumar
"""

from itertools import combinations
def mostVisitedPattern(username, timestamp, website):
        
        users = {}
        for user, time, web in sorted(zip(username, timestamp, website), key = lambda x: (x[0], x[1])):
            if user in users:
                users[user].append(web)
                continue
            users[user] = [web]
        
        rec = {}
        
        for user, web in users.items():
            matches = set(combinations(web, 3))
            for match in matches:
                if match in rec:
                    rec[match] += 1
                    continue
                rec[match] = 1
        return list(max(sorted(rec), key= rec.get))
    
username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]
res = mostVisitedPattern(username, timestamp, website)
print(res)