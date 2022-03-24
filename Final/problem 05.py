# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 20:29:44 2022

@author: Silviu
Problem 5
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    keys = []
    temp = {}
    
    for value in aDict.values():
        if value in temp.keys(): 
            temp[value] += 1
        else:
            temp[value] = 1
    
    for key in aDict.keys():
        if ( temp[ aDict[key] ] == 1):
            keys.append(key)            
            
    return sorted(keys)

dict1 = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
print( uniqueValues( dict1 ) )

dict2 = {1: 1, 2: 1, 3: 1}
print( uniqueValues( dict2 ) )
    