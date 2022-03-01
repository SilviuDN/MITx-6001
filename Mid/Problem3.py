# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 17:49:46 2022

@author: User
"""
#Problem 3
#Write a recursive Python function, given a non-negative integer N, to count and return the number of occurrences of the digit 7 in N.

def count7(N):
    '''
    N: a non-negative integer
    '''
    if N == 0: return 0
    if N%10 == 7:
        return 1 + count7(N//10)
    else:
        return count7(N//10)

print ( count7(7)) 