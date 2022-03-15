# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 13:02:55 2022

@author: User
"""

def intToString(n):
    digits = '0123456789'
    if n == 0: return '0'
    res = ''
    while n> 0:
        res = digits[ n%10 ] + res
        n //= 10
    return res

print( intToString(12345) )