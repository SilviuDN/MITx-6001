# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 19:15:37 2022

@author: Silviu
"""

from sympy import *

import numpy as np

x = Symbol('x')

y = x**2 + 1

yprime = y.diff(x)

print(yprime)

# =============================================================================
# y = input("f = ")
# =============================================================================
y = x**2-2**x
print("f' = ", y.diff(x))