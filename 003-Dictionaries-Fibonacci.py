# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 13:48:15 2022

@author: Silviu
"""
d={1:2, 2:2}

def fibEfficient(n, d):
    if n in d:
        return d[n]
    else:
        d[n] = fibEfficient(n-1, d) + fibEfficient(n-2, d)
        return d[n]
    
print( fibEfficient(500, d) )
        
    