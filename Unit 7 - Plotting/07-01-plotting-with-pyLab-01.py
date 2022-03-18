# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 21:09:35 2022

@author: Silviu - MIT Grimson
"""

import pylab as plt

xValues = []
yCuadratic = []
yCubic = []

for i in range(-30, 30):
    xValues.append(i)
    yCuadratic.append(i*i)
    yCubic.append(i*i*i)
    
plt.plot( xValues, yCuadratic )    
plt.plot( xValues, yCubic )
