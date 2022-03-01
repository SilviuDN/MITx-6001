# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 18:38:33 2022

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

def howMany(aDict):
    '''
    aDict: a dictionary
    '''
    
    helper = {}
    
    for key in aDict:
        temp = aDict[key]
        if aDict[key] not in helper.keys():
            helper[ temp ] = 1
        else:
            helper[ temp ] = helper[ temp ] + 1
    return helper

dic = {1:2, 2:3, 4:2}
print( howMany( dic ) )