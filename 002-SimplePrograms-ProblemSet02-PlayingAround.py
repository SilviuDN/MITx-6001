# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 00:18:15 2022

@author: User
"""

def previousBalance(currentBalance, annualInterestRate, fixedPayment):
    return ( currentBalance - fixedPayment ) * ( 1 + annualInterestRate / 12.0)

balance = 3329
annualInterestRate = 0.2
fixedPayment = 300

for i in range(12):
    balance = previousBalance(balance, annualInterestRate, fixedPayment)
    print(balance)