# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 13:09:03 2022

@author: User
"""

#Scope exercise

# Global scope vs Function Scope
# =============================================================================
# def f(x):
#     print('x in functie inainte de incrementare.', x)
#     x = x+1
#     print('x in functie dupa incrementare.', x)
#     return x
# x=3
# print("x in global: ", x)
# f(x)
# print("x in global: ", x)
# =============================================================================


# Global Scope, Outer Function Scope, Inner Function Scope
# =============================================================================
# def f1(x):
#     x=x+1
#     print("in f1:", x)
#     return x
#     
# def f2(x):
#     x=x+1
#     print("in f2:", x)
#     return x
# 
# x=0
# print("x in global: ", x)
# f2(f1(x))
# print("x in global: ", x)
# =============================================================================


# Implicit return
# =============================================================================
# def functionOfNoReturn():
#     print('inside')
#     
# print(functionOfNoReturn())
# =============================================================================


# UnboundVariableException
# =============================================================================
# def g(y):
#     x=7
#     x += 1
#     
# x=5
# g(x)
# print(x)
# =============================================================================
    

# UnboundVariableException
#def h(y):
#    x += 1

#x=5
#h(x)
#print(x)