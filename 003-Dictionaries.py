# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 13:33:38 2022

@author: Silviu
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for key in aDict:
        count += len( aDict[key] )
    return count

print(how_many(animals))

def how_many2(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    sumValues = sum(aDict.values(), [])
    return(len(sumValues)) 

print(how_many2(animals))

#Method 2
def how_many3(aDict):
    count = 0
    for key in aDict.keys():
        count += len(aDict[key])
    return count

print('3rdmethod:', how_many3(animals))


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    maxLen = -1
    for key in aDict:
        if len( aDict[key] ) > maxLen:
            res = key
            maxLen = len( aDict[key] )
    return res
       
    
    
print( biggest(animals) )