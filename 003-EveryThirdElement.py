# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 21:21:20 2022

@author: Silviu
"""

def oddPositioned(tup):
    res = ()
    index = 1
    for el in tup:
        if index % 2: res += (el,)
        index += 1
    return res
        
print( oddPositioned( ('I', 'am', 'a', 'test', 'tuple') ) )


