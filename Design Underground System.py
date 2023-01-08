# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 11:11:05 2023

@author: Avinash Kumar
"""

class UndergroundSystem:

    def __init__(self):
        self.userCheckIn = {}
        self.userCheckOut = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.userCheckIn[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        prevStation, prevTime = self.userCheckIn[id]
        code = prevStation + "_" + stationName
        prevSum = 0
        prevCount = 0
        if code in self.userCheckOut:
            prevSum, prevCount = self.userCheckOut[code]
        self.userCheckOut[code] = [t - prevTime + prevSum, prevCount + 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        code = startStation + "_" + endStation
        sum, length = self.userCheckOut[code]
        return float(sum/ length)
        


# Your UndergroundSystem object will be instantiated and called as such:
obj = UndergroundSystem()
obj.checkIn(45,"Leyton",3)
obj.checkIn(32,"Paradise",8)
obj.checkIn(27,"Leyton",10)
obj.checkOut(45,"Waterloo",15)
obj.checkOut(27,"Waterloo",20)
obj.checkOut(32,"Cambridge",22)
print(obj.getAverageTime("Paradise","Cambridge"))
print(obj.getAverageTime("Leyton","Waterloo"))
obj.checkIn(10,"Leyton",24)
print(obj.getAverageTime("Leyton","Waterloo"))
obj.checkOut(10,"Waterloo",38)
print(obj.getAverageTime("Leyton","Waterloo"))