# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 17:14:08 2022

@author: User
"""

def fib(n):
    if n==0 or n ==1: return 1
    return fib(n-1) + fib(n-2)

for k in range(5):
    print(fib(k))
    
    
print()

# Decide if a string is a palindrome

def toChars(s):
    s = s.lower()
    res = ''
    for char in s:
        if char in 'qwertyuioplkjhgfdsazxcvbnm':
            res += char
    return res

def isPalindrome(prop):
    if str( len(prop ) ) in '01': return True
    if prop[0] != prop[ len(prop) - 1 ]: return False
    return isPalindrome( prop[ 1 : len(prop) ])

def reducesToPalindrome(prop):
    return isPalindrome( toChars( prop ))
    
    
    
print( isPalindrome('') )        
print( isPalindrome('a') )    
print( isPalindrome('aba') )    
print( isPalindrome('abbcbba') )    
print( isPalindrome('abc') )    
print( isPalindrome('abca') )    
print( isPalindrome('abaa') )    
print( isPalindrome('aaaa') )

print( reducesToPalindrome('') )        
print( reducesToPalindrome('a') )    
print( reducesToPalindrome('a 12ba') )    
print( reducesToPalindrome('abbc345bba') )    
print( reducesToPalindrome('a;;/.bc) ')    )
print( reducesToPalindrome(';/;abca/;/') )    
print( reducesToPalindrome('/;/abaa') )    
print( reducesToPalindrome('aa 87aa') )
