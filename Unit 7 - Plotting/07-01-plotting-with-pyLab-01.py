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
  
plt.figure('quadratic')  
plt.title('quadratic')
plt.xlabel("abscisa")
plt.ylabel("ordonata")
plt.plot( xValues, yCuadratic ) 


plt.figure('cubic')   
plt.plot( xValues, yCubic )


plt.figure('cubic')
plt.xlabel("abscisa")
plt.ylabel("ordonata")
plt.title('cubic')


plt.figure('quadratic')
plt.clf()
plt.title('quadratic')
plt.plot( xValues, yCuadratic ) 

