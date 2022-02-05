# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 15:49:32 2022

@author: Silviu
"""

# =============================================================================
# def odd(x):
#     '''
#     x: int
# 
#     returns: True if x is odd, False otherwise
#     '''
#     return  False if x % 2 == 0 else True
# =============================================================================


# =============================================================================
# # Calculate the power base**exp
# def recurPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
#  
#     returns: int or float, base^exp
#     '''
#     # Your code here
#     return ( 1 if exp == 0 else base * recurPower(base, exp - 1) )
# 
# print(recurPower(2, 10))
# 
# 
# def iterPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
#  
#     returns: int or float, base^exp
#     '''
#     # Your code here
#     acum = 1
#     while( exp > 0 ):
#         acum *= base
#         exp -= 1
#     return acum
# 
# print(iterPower(2, 10))
# =============================================================================
        

# gcd --> greatest common divisor of two given positive numbers
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    while(a*b != 0):
        if a<b:
            b -= a
        else:
            a -= b
    return a + b

print( gcdIter( 70,12 ))


def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a*b == 0: return a+b
    return( gcdRecur( min(a,b), abs(a-b) ))
 
print( gcdRecur( 70,12 ))   
print( gcdRecur( 0,12 ))    
print( gcdRecur( 9,12 ))    
print( gcdRecur( 18,12 ))    
print( gcdRecur( 1,12 ))    
print( gcdRecur( 10,12 ))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    