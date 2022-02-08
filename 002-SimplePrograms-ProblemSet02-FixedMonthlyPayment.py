# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 23:54:23 2022

@author: User
"""

months = 12


def previousBalance(currentBalance, annualInterestRate, fixedPayment):
    return ( currentBalance - fixedPayment ) * ( 1 + annualInterestRate / 12.0)

def coversCredit(balance, annualInterestRate, fixedPayment):
    counter = 0
    while balance > fixedPayment:
        counter += 1
        balance = previousBalance(balance, annualInterestRate, fixedPayment)
    if counter < 12: return True 
    else: return False
   
def lowestMonthlyPayment(balance, annualInterestRate):
    if balance < 120: return 10
    fixedPayment = balance // 120 *10
    while ( coversCredit(balance, annualInterestRate, fixedPayment) == False):
        fixedPayment += 10
    return fixedPayment
    

print('Lowest Payment: ' + str( lowestMonthlyPayment(balance, annualInterestRate)) )


print('Lowest Payment: ' + str( lowestMonthlyPayment(100, 0.2)) )
print('Lowest Payment: ' + str( lowestMonthlyPayment(120, 0.2)) )
print('Lowest Payment: ' + str( lowestMonthlyPayment(3926, 0.2)) )

#print(3329, coversCredit(3329, 0.2, 310) )
#print(3329, coversCredit(3329, 0.2, 300) )

#print(4773, coversCredit(4773, 0.2, 440) ) 
#print(4773, coversCredit(4773, 0.2, 430) ) 

#print(3926, coversCredit(3926, 0.2, 360) )       
#print(3926, coversCredit(3926, 0.2, 350) ) 