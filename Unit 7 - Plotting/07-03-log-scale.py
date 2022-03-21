# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 23:16:52 2022

@author: Silviu - MIT Grimson
"""

import pylab as plt

xValues = []
yExp = []
yCubic = []

for i in range(0, 30):
    xValues.append(i)
    yExp.append(2**i)
    yCubic.append(i*i*i)

plt.figure('cubic - exponential')
plt.clf()
plt.yscale('log')
plt.ylim(0, 10000)
plt.subplot(211)
plt.plot( xValues, yExp, 'r-', label = 'exp', linewidth = 2.0 )
plt.subplot(212)
plt.plot( xValues, yCubic, 'go', label = 'cubic', linewidth = 5.0  ) 
plt.legend(loc = 'lower right')

#plt.legend()