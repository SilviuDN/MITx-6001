# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 17:31:46 2022

@author: User
"""

x=1
y=2
x,y = y,x
print(x,y)

stuff  = ["iQ"]
for thing in stuff:
    if thing == 'iQ':
         print("Found it")
         
         
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print(Square(-12))