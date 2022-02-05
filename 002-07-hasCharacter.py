# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 17:36:05 2022

@author: User
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    length = len(aStr)
    if length == 0: return False
    if length == 1:
        if char == aStr[0]: return True
        else: return False
    if length == 2:
        if char == aStr[0]: return True
        
    if char < aStr[length // 2]: return isIn( char, aStr[: length // 2])
    return isIn( char, aStr[length // 2 : ])

print(isIn('a', '') )
print(isIn('e', 'e') )
print(isIn('e', 'abc') )
print(isIn('e', 'abcde') )
print(isIn('e', 'abcdef') )
print(isIn('e', 'abcdefg') )
print(isIn('e', 'efg') )
