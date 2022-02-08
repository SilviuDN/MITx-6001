# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 22:21:38 2022

@author: Silviu
"""
months = 12
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
          
          
def remainingBalance(balance, annualInterestRate, monthlyPaymentRate, month):
    if month == 0: return balance
    return remainingBalance(balance, annualInterestRate, monthlyPaymentRate, month-1) * (1 - monthlyPaymentRate) * ( 1 + annualInterestRate / 12.0 )


print('Remaining balance: ' + str( round( remainingBalance(balance, annualInterestRate, monthlyPaymentRate, 12) , 2) ))