# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 19:36:36 2022

@author: SilviuD
"""

#https://www.codewars.com/kata/5a331ea7ee1aae8f24000175

def returnColor(color1, color2):
    if color1 == color2: return color1
    if 'R' not in color1+color2: return 'R'
    if 'G' not in color1+color2: return 'G'
    if 'B' not in color1+color2: return 'B'
    
def reduceRow(string):
    stringLength = len(string)
    if stringLength == 1: return string
    res=''
    for k in range( stringLength - 1 ):
        res += returnColor(string[k], string[k+1])
    return res

def triangle(string):
    while len(string) > 1:
        string = reduceRow(string)
    return string

print( triangle( 'BBRRBRGBR' ))