# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 20:10:17 2022

@author: Silviu
Problem 4
"""

def primes_list(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    # Your code here
    def isPrime(number):
        if number < 2: return False
        if number == 2: return True
        for i in range(number//2):
            if number % (i+2) == 0:
                return False
        return True       
    res = []
    for i in range(N+1):
        if isPrime(i): res.append(i)
    return res
        

for i in range (29):   
    print( i, ' ', primes_list(i) )
