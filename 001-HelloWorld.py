# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 19:31:49 2022

@author: SilviuDN
"""

#s='azcbobobegghakl'

# =============================================================================
# res = 0
# =============================================================================


#Problem 01

# =============================================================================
# for char in s:
#     if char in 'aeiou':
#         res += 1
#         
# print('Number of vowels:',res)
# =============================================================================


#Problem 02
# =============================================================================
# Even if it worked in local, I had problems with:
#     incomplete code pasted in the sandbox
#     result format ( did not use concatenation )
# =============================================================================

# =============================================================================
# s='bzobooobobtbo'
# 
# res=0
# for k in range (len(s) - 2):
#     if s[k] == 'b' and s[k+1] == 'o' and s[k+2] == 'b':
#         res += 1
# 
# print("Number of times 'bob' occurs is: " + str(res) )
# =============================================================================

#Problem 03
# =============================================================================
# Longest substring of:
#     consecutive letters - changed to
#     alphabetically ordered letters
# =============================================================================

s='abcabcdlefghijzz'
#s = 'azcbobobegghakl'
#s = 'abcbcd'

import string

def index(letter):
    return string.ascii_lowercase.index( letter.lower())

def areConsecutiveLetters( letter1, letter2 ):
    dif = index(letter2) - index( letter1 )
    #return dif == 1
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





# =============================================================================
# for k in range(len(s) - 1):
#     tempMax = 1
#     while()
# =============================================================================






#Problem 04



#Problem 05


