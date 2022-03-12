# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:16:07 2022

@author: Silviu
"""

'''
genPrimes is a generator that returns a sequence of prime numbers on succesives calls
'''

def genFib():
    fib1 = 0
    fib2 = 1
    while True:
        next = fib1 + fib2
        yield next
        fib1 = fib2
        fib2 = next
        

fib = genFib()
print(fib)

print( fib.__next__() )

def genPrimes():
    primesList = [2]
    while True:
        yield primesList
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
            
        
    