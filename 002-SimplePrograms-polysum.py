# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 18:02:47 2022

@author: User
"""
import math

def polysum(n, s):
    return round( area(n, s) + perimeter(n, s)**2 , 4 )

def area(n, s):
    return 0.25*n*s*s/math.tan(math.pi/n)

def perimeter(n, s):
    return n*s
