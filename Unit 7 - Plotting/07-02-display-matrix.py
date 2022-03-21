# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 23:16:52 2022

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

plt.figure('quadratic - cubic')
plt.clf()
plt.ylim(-100, 100)
plt.subplot(211)
plt.plot( xValues, yCuadratic, 'r-', label = 'quadratic', linewidth = 2.0 )
plt.subplot(212)
plt.plot( xValues, yCubic, 'go', label = 'cubic', linewidth = 5.0  ) 
plt.legend(loc = 'lower right')
#plt.legend()