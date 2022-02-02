# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 19:22:37 2022

@author: User
"""

# Problem solved:    
# https://www.codewars.com/kata/54d496788776e49e6b00052f


def multiplesSum(p, arr):
    sum = 0
    if len(arr) == 0: return sum
    for k in range( len(arr) ): 
        if( arr[k] % p == 0):
            sum += arr[k]
    return sum

#print(multiplesSum( 3, [12, 15]  ))

def isPrime( number ):
    if number == 0: return False
    if number == 1: return False
    if number == 2: return True
    res = True
    for k in range(2, number // 2 + 1):
        if number % k == 0: res = False
    return res

def primesSmallerThan( number ):
    if number <= 1: return []
    if number == 2: return [2]
    res = []
    for k in range( number ):
        if isPrime(k): res.append( k )
    return res

def sum_for_list( arr ):
     res=[]
     maxOfArray = max(arr) // 2 + 1
     primes = primesSmallerThan(maxOfArray)
     stop = len(primes)
     for i in range( 0 , stop ):
         k = primes[ i ]
         if isPrime( k ):
             tempSum = 0
             tempSum = multiplesSum( k, arr )
             if multiplesSum( k, arr ) != 0:
                 res.append( [k, tempSum] )
     return res

def sum_for_list2( arr ):
     res=[]
     stop = max(arr) // 2 + 1
     for k in range( 1 , stop ):
         if isPrime( k ):
             tempSum = 0
             tempSum = multiplesSum( k, arr )
             if multiplesSum( k, arr ) != 0:
                 res.append( [k, tempSum] )
     return res
 
answer =  sum_for_list( [12, 15] )

#print( primesSmallerThan(25) ) 

print( answer )

print( isPrime(4) )

























#homework:
    #https://www.codewars.com/kata/5993c1d917bc97d05d000068