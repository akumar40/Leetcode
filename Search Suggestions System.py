# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 00:39:20 2022

@author: Avinash Kumar
"""

def suggestedProducts(products, searchWord):
        res = []
        match = []
        n = -1
        for idx in range(len(searchWord)):
            if n == 0:
                res.append([])
                continue
            char = searchWord[:idx+1]
            if n > 0:
                match = list(filter(lambda x: x[:idx+1] == char, match))
            else:
                match = list(filter(lambda x: x[:idx+1] == char, products))
            n = len(match)
            res.append(sorted(match)[:3])
        return res
    
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
res = suggestedProducts(products, searchWord)
print(res)