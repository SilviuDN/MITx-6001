# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 01:10:20 2022

@author: User
"""
months = 12
step =0.01

def previousBalance(currentBalance, annualInterestRate, fixedPayment):
    return ( currentBalance - fixedPayment ) * ( 1 + annualInterestRate / 12.0)

def coversCredit(balance, annualInterestRate, fixedPayment):
    counter = 0
    while balance > fixedPayment:
        counter += 1
        balance = previousBalance(balance, annualInterestRate, fixedPayment)
    if counter < 12: return True 
    else: return False
   
def lowestMonthlyPayment(balance, annualInterestRate, step=0.01):
    if balance < 12 * step: return step
    minFP = balance // (12 * step) * step
    maxFP = balance // 2
    while( maxFP - minFP >= 0.01):
        fixedPayment = ( minFP + maxFP ) / 2
        if( coversCredit(balance, annualInterestRate, fixedPayment) == False ):
            minFP = fixedPayment
        else: 
            maxFP = fixedPayment
    return round( fixedPayment, 2)
    
balance = 999999
annualInterestRate = 0.18


print('Lowest Payment: ' + str( lowestMonthlyPayment(balance, annualInterestRate)) )


print('Lowest Payment: ' + str( lowestMonthlyPayment(320000, 0.2)) )
print('Lowest Payment: ' + str( lowestMonthlyPayment(999999, 0.18)) )

