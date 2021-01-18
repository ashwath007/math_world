import math as m
import os
import sys

class conditionprob(): //Parent Class
    def __init__(self,x,y,prop):
        self.x = x
        self.y = y
        self.prop = prop
    def cal(self):
        return self.x*self.y

class poppass(conditionprob): //Children Class
    def ok():
        print("END")


e = conditionprob(10,22,90.89)
print(e.__dict__)
print(e.cal())
ob = poppass(10,222,232.89)
print(ob.cal())