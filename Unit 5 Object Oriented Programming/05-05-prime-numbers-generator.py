# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:16:07 2022

@author: Silviu
"""

'''
genPrimes is a generator that returns a sequence of prime numbers on succesives calls
'''
def genPrimes():
    primesList = [2]
    while True:
        yield primesList[-1]
        n = primesList[-1] + 1
        while True:
            isPrime = True
            for prime in primesList:
                if n%prime == 0:
                    isPrime = False
            if isPrime == True: 
                primesList.append(n)
                break
            n += 1
        
primes = genPrimes()

print( primes.__next__() )
            
    
        
    
# OFFICIAL MIT SOLUTION
def genPrimes2():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
            
        
primes2 = genPrimes2()

print( primes2.__next__() )