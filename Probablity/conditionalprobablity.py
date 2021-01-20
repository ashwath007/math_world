import math as m
import os
import sys
import basic as bs

class conditionprob(): #Parent Class
    def __init__(self,x,y,prop):
        self.x = x
        self.y = y
        self.prop = prop
    def cal(self):
        return self.x*self.y

class poppass(conditionprob): #Children Class
    def ok():
        print("END")


res = bs.sum_of_error([5,6,7],[90,6,9])
print(res.cal())

# e = conditionprob(10,22,90.89)
# print(e.__dict__)
# print(e.cal())
# ob = poppass(10,222,232.89)
# print(ob.cal())