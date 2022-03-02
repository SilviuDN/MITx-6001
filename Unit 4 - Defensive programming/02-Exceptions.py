# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:47:21 2022

@author: Silviu
"""

a = ''
while True and a != 'x':
    try:
        n = input( "Give me an integer! ")
        n == int(n)
        break
    except ValueError:
        a = input( "Not an integer. Press 'x' to exit or anything else to continue. " )
    else:
        print('Nice integer!')