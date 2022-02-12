# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 11:33:18 2022

@author: Silviu
"""
#Ex1: return absolute value 
testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

applyToEach(testList, abs)

print(testList)


#Ex2: return successor
testList = [1, -4, 8, -9]

def addOne(x): return x+1

applyToEach(testList, addOne)

print(testList)


#Ex3: return square
testList = [1, -4, 8, -9]

def square(x): return x*x

applyToEach(testList, square)

print(testList)