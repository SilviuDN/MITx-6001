# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 18:02:47 2022

@author: Silviu

"""
import math

def polysum(n, s):
    '''
    Parameters
    ----------
    n : int
        number of sides of a regular polygon
        
    s : float
        side length of a regular polygon

    Returns
    -------
    TYPE: float
        sum of square of the perimeter with the area of the regular polygon, rounded to 4 decimals

    '''
    return round( area(n, s) + perimeter(n, s)**2 , 4 )

def area(n, s):
    '''
    Parameters
    ----------
    n : int
        number of sides of a regular polygon
        
    s : float
        side length of a regular polygon

    Returns
    -------
    TYPE: float
        area of the regular polygon.

    '''
    return 0.25*n*s*s/math.tan(math.pi/n)

def perimeter(n, s):
    '''
    Parameters
    ----------
    n : int
        number of sides of a regular polygon
        
    s : float
        side length of a regular polygon

    Returns
    -------
    TYPE: float
        perimeter of the regular polygon

    '''
    return n*s
