# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 18:09:52 2022

@author: User
"""

# =============================================================================
# Write a Python function that returns 
# a list of keys in aDict 
# that map to integer values that are unique 
# (i.e. values appear exactly once in aDict). 
# The list of keys you return should be sorted in increasing order. 
# (If aDict does not contain any unique values, you should return an empty list.)
# =============================================================================

def uniqueValues(aDict):
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

def hasValue1(aDict):
    res = []
    for key in aDict:
        if aDict[key] == 1:
            res.append( key )
    return res

def hasValue(searchedValue, aDict):
    res = []
    for key in aDict:
        if aDict[key] == searchedValue:
            res.append( key )
    return res

#print( uniqueValues( dic ) )
#print( hasValue(1,  uniqueValues( dic ) ) )

def keysMappedToUniquesValues( aDict ):
    res = []
    uniques = uniqueValues( aDict )
    print ( uniques )
    for key in aDict:
        print( aDict[key] )
        if aDict[key] in uniques:
            res.append(key)
    return res

print( keysMappedToUniquesValues( dic ) )