# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 19:09:58 2022

@author: User
"""

# Problem 7
# =============================================================================
# Write a function called general_poly, that meets the specifications below. 
# For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because .
# =============================================================================

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    
    def helper(val):
        res = 0
        n = len( L )
        for coefficient in L:
            n=n-1
            res = res + coefficient * val**n
        return res
    
    return helper

print( general_poly([1, 2, 3, 4])(10) )