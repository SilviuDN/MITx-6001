# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 13:14:08 2022

@author: Silviu and MIT
"""

def isSubset(A, B):
    if len(A) == 0: return True
    if len( B ) == 0: return False
    for elemA in A:
        isInB = False
        for elemB in B:
            if elemA == elemB:
                isInB = True
                break
        if isInB == False: return False
    return True

print( isSubset( [], [1,2,3,4] ) )
print( isSubset( [1,2,3], [] ) )
print( isSubset( [1,2,3], [1,2,3] ) )
print( isSubset( [1,2,3], [1,2,3,4] ) )
print( isSubset( [1,2,3,5], [1,2,3,4] ) )

def intersect(A, B):
    inter = []
    for elemA in A:
        for elemB in B:
            if elemA == elemB: inter.append(elemA)
    res=[]    
    for elem in inter:
        if not( elem in res ): res.append(elem)
    return res

print( intersect( [], [1,2,3,4] ) )
print( intersect( [1,2,3,5], [] ) )
print( intersect( [1,2,3], [1,2,3] ) )
print( intersect( [1,2,3], [1,2,3,4] ) )
print( intersect( [1,2,3,5], [1,2,3,4] ) )