# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 19:02:59 2022

@author: User
"""

def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    a = 0
    n=len(L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
                a += 1
    print("Final L: ", L, a, n*(n+1)/2)
    
#swapSort([1,2,3,4,5,6,7,8,9])
#swapSort([1,2,3,4,5,6,7,8,9,10])

swapSort([4,3,2,1])