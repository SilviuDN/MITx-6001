# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 17:59:02 2022

@author: User
"""

#Problem 4
# =============================================================================
# Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters. 
# For example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]
# =============================================================================

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    res = []
    for element in aList:
        if len(element) < 4:
            res.append(element)
    return res

print( lessThan4( ["apple", "cat", "dog", "banana"] ) )