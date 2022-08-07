# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 23:48:54 2022

@author: Avinash Kumar
"""

def reorderLogFiles(logs):
        llog = {}
        dlog = []
        for idx, log in enumerate(logs):
            text = log.split(' ')
            if ord(text[1][0])  >= 48 and ord(text[1][0]) <= 57:
                dlog.append(log)
            else:
                idx = log.index(' ')
                if text[0] in llog:
                    llog[' '.join([text[0], str(idx)])] = log[idx+1:]
                    continue
                llog[text[0]] = log[idx+1:]
        res = []
        for key, value in sorted(llog.items(), key = lambda x: (x[1], x[0])):
            idx = key.find(' ')
            if idx > -1:
                res.append(' '.join([key.split(' ')[0], value]))
                continue
                
            res.append(' '.join([key, value]))
        res += dlog
        return res
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
res = reorderLogFiles(logs)
print(res)