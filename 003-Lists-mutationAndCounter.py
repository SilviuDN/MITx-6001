# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 21:21:31 2022

@author: Silviu
"""

#l1 is a list => mutable => the counter is increased and the loops skips 2
l1 = [1,2,3,4]
l2 = [1,2,5,6]

def removeDUps(l1, l2):
        for e in l1:
            if e in l2:
                l1.remove(e)
                
removeDUps(l1, l2)


l3=[1,2,3,4]
l4=[1,2,5,6]

def remove_duplicates(l1, l2):
    l1_copy = l1[:]
    for e in l1_copy:
        if e in l2:
            l1.remove(e)
            
remove_duplicates(l3, l4)

l6 = [1,2,3]
l7 = [4,5,6,7]
l8 = l6 + l7

print(l8)


l9 = [1,2,3,4,5,6,7,8,9]

def verifyListMutability(li):
    for el in li:
        print(li)
        print(el)
        li.remove(el)
        
verifyListMutability(l9)