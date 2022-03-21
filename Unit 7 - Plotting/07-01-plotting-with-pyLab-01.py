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
  
# =============================================================================
# plt.figure('quadratic')  
# plt.title('quadratic')
# plt.xlabel("abscisa")
# plt.ylabel("ordonata")
# plt.plot( xValues, yCuadratic ) 
# 
# 
# plt.figure('cubic')   
# plt.plot( xValues, yCubic )
# 
# 
# plt.figure('cubic')
# plt.xlabel("abscisa")
# plt.ylabel("ordonata")
# plt.title('cubic')
# =============================================================================


# =============================================================================
# plt.figure('quadratic')
# plt.clf()
# plt.ylim(0, 1000)
# plt.title('quadratic')
# plt.plot( xValues, yCuadratic ) 
# 
# plt.figure('cubic')
# plt.clf()
# plt.ylim(0, 1000)
# plt.title('cubic')
# plt.plot( xValues, yCubic ) 
# =============================================================================

#-0^--
#subplot(nrRows, nrColumns,which location to use)
plt.figure('quadratic - cubic')
plt.clf()
plt.subplot(211)
plt.ylim(-100, 100)
plt.plot( xValues, yCuadratic, 'r-', label = 'quadratic', linewidth = 2.0 )
plt.plot( xValues, yCubic, 'go', label = 'cubic', linewidth = 5.0  ) 
plt.legend(loc = 'lower right')
#plt.legend()


