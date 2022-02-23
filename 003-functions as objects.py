# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:54:59 2022

@author: User
"""

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

print( applyEachTo([inc, square, halve, abs], -3) )
print( applyEachTo([inc, square, halve, abs], 3.0) )
print( applyEachTo([inc, max, int], -3) )
