# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 11:11:50 2022

@author: Silviu
"""

L = [1,-2,3,-4]

L2 = map(abs, L)

print('Lista initiala L este: ', L)

print('Lista L mapata este L2: ', L2)


# =============================================================================
# print('Elementele din L2 sunt: ')
# for el in L2:
#     print(el)
# 
# print('Dupa parcurgere L2 devine lista?!??? Arata asa:', L2)
# =============================================================================

L3 = list( L2 )
print('mapObjectul L2 converted to list este L3: ', L3)

List1 = [10,20,30,40]
List2 = [15,15,35,35]

minimumList = list( map( min, List1, List2 ) )
print(minimumList)