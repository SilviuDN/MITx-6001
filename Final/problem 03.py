# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 19:53:19 2022

@author: Silviu
"""
def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    sum = 0
    areSomeDigits = False
    for char in s:
        try:
            num = int(char)
        except ValueError:
            pass
        else:
            sum += num
            areSomeDigits = True
           
    if areSomeDigits == False:
        raise ValueError
    else:
        return sum
     
print( sum_digits('1') )