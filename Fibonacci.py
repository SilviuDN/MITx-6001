# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:33:39 2022

@author: Silviu
"""

def Fibonacci(n):
    if n==1 or n == 0: return 1
    return ( Fibonacci ( n-2 ) + Fibonacci(n-1) )

for i in range(10):
    print( Fibonacci(i) )