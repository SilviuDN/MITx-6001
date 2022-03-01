# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 18:40:10 2022

@author: Silviu
"""


#Problem 5
# =============================================================================
# Write a Python function that returns 
# a list of keys in aDict 
# that map to integer values that are unique 
# (i.e. values appear exactly once in aDict). 
# The list of keys you return should be sorted in increasing order. 
# (If aDict does not contain any unique values, you should return an empty list.)
# =============================================================================

dic = {1:2, 2:3, 4:2, 5:4, 6:5, 7:5}

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    res = []
    for key in aDict:
        if howMany(aDict[key], aDict) == 1:
            res.append(key)        
    return res

def howMany(a, aDict):
    res = 0
    for key in aDict:
        if aDict[key] == a: 
            res = res + 1
    return res

#print ( howMany(2, dic) )
print ( uniqueValues( dic) )
