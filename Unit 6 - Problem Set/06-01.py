# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 18:37:50 2022

@author: User
"""

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if e < L[i]:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if e > L[i]:
            return False
    return False


print( search( [], 3))
print( newsearch( [], 3))


print( search( [1,2,4], 3))
print( newsearch( [1,2,4], 3))


print( search( [1,2,3,4], 3))
print( newsearch( [1,2,3,4], 3))


print( search( [1], 3))
print( newsearch( [3], 3))

print('###########################')
print( search( [1,3], 3))
print( newsearch( [1,4], 3))
print( search( [1,3], 1))
print( search( [1,3], 1))