# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 13:08:43 2022

@author: Silviu and MIT
"""

def factorial_iter(n):
    fact = 1
    i = 1
    while i < n+1:
        fact *= i
        i += 1
    return fact

print( factorial_iter(3) )


def fact_rec(n):
    if n <= 1: return 1
    return n * fact_rec( n-1 )

print( factorial_iter(3) )

