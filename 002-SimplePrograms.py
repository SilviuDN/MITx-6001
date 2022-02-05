# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 19:42:35 2022

@author: Silviu
"""

#Exercise "Guess my number"

print("Please think of a number between 0 and 100! ")

# =============================================================================
# inf = 0
# sup = 100
# guess = 50
# res = input("Is your secret number " + str(guess) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
# 
# while( res != "c" ):
#     if res == 'h': sup = guess
#     elif res == 'l': inf = guess  
#     else:
#         print("Sorry, I did not understand your input.")
#         res = input("Is your secret number " + str(guess) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
#         continue
#     guess = (sup + inf) // 2
#     res = input("Is your secret number " + str(guess) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
# 
# print("Game over. Your secret number was: " + str( guess ))
# =============================================================================
    

#Exercise eval quadratic
# =============================================================================
# def evalQuadratic(a, b, c, x):
#     '''
#     a, b, c: numerical values for the coefficients of a quadratic equation
#     x: numerical value at which to evaluate the quadratic.
#     '''
#     return a*x**2+b*x+c == 0
#     
# import math
# def solveQuadratic(a, b, c, x):
#     '''
#     a, b, c: numerical values for the coefficients of a quadratic equation
#     x: numerical value at which to evaluate the quadratic.
#     '''
#     # Your code here
#     if a==0:
#         if b==0:
#             if c==0: return "Anything works! :))"
#             else: return "Never gonna happen!"
#         else:
#             return -c / a
#     else:
#         delta = b**2 - 4*a*c
#         if delta<0: return "Does not happen in real life! ;)"
#         elif delta==0: return -b/(2*a)
#         else: return "There are two real solutions: " + str( (-b - math.sqrt(delta) ) / (2*a) )\
#             + " and " + str( (-b + math.sqrt(delta) ) / (2*a) )
#     
# print( solveQuadratic(1,3,2,0) )
# print( evalQuadratic(1,3,2,0) )
# =============================================================================



