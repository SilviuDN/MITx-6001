# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 19:42:35 2022

@author: Silviu
"""

#Exercise "Guess my number"

print("Please think of a number between 0 and 100! ")

inf = 0
sup = 100
guess = 50
res = input("Is your secret number " + str(guess) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while( res != "c" ):
    if res == 'h': sup = guess
    elif res == 'l': inf = guess  
    else:
        print("Sorry, I did not understand your input.")
        res = input("Is your secret number " + str(guess) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        continue
    guess = (sup + inf) // 2
    res = input("Is your secret number " + str(guess) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

print("Game over. Your secret number was: " + str( guess ))
    