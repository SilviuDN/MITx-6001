# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 20:45:22 2022

@author: Silviu
"""

def getData(aTuple):
    nums=()
    words=()
    for t in aTuple:
        nums += (t[0],)
        if t[1] not in words:
            words += (t[1],)
    minNums = min(nums)
    maxNums = max(nums)
    uniqueWords = len(words)
    return (minNums, maxNums, uniqueWords, words)

print( getData( ( ('1','a'),  ('2','b'), ('3','cde'), ('4','cde') ) ) )

(mini, maxi, uni, words) = getData( ( ('1','a'),  ('2','b'), ('3','cde'), ('4','cde') ) )

print(mini, maxi, uni, words)



tup = ('I', 'am', 'a', 'test', 'tuple')

def oddTuples(tup):
    res = ()
    index = 1
    for el in tup:
        if index % 2: res += (el,)
        index += 1
    return res    

def oddTuples2(tup):
    return tup[::2]

print(oddTuples(tup))
print(oddTuples2(tup))