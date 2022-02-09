# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 16:37:17 2022

@author: Silviu
"""
s='azcbobobegghakl' 


# 2'nd solution

maxLenght = 1
longestSubstring = ''
tempSubstring = s[0]

for i in range( len(s) - 1 ):
    if s[i] <= s[i+1]:
        tempSubstring += s[i+1]
        if len( tempSubstring ) > maxLenght:
            longestSubstring = tempSubstring
            maxLenght = len( tempSubstring )
    else: tempSubstring = s[i+1]
    
print('Longest substring in alphabetical order is: ' + longestSubstring)
        
        

#1'st solution

import string


def index(letter):
    return string.ascii_lowercase.index( letter.lower())

def areConsecutiveLetters( letter1, letter2 ):
    dif = index(letter2) - index( letter1 )
    return  dif >= 0

def howManyConsecutiveLetters( sentence, pos ):
    if pos >= len( sentence ): return 0
    length = 1
    if pos == len( sentence ) - 1 : return length
    while( areConsecutiveLetters ( sentence[pos + length - 1], sentence[pos + length] )):
        length += 1
        if pos + length == len(sentence):
            break
    return length


def longestString(s):
    firstCharPos = 0
    if len(s) == 0: return ''
    if len(s) == 1: return s
    pos = 0
    maxLen = 1
    while(pos < len(s) ):
        tempCandidate = howManyConsecutiveLetters(s, pos)
        if maxLen < tempCandidate:
            maxLen = tempCandidate
            firstCharPos = pos
        pos = pos + tempCandidate
    return( s[ firstCharPos : firstCharPos+maxLen ] )
    
print('Longest substring in alphabetical order is: ' + longestString(s))