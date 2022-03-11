# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:09:38 2022

@author: Silviu
"""

#GENERATORS

#Creating my own GENERATOR
def generatorTest():
    yield 1
    yield 2
    
foo = generatorTest()

print( foo.__next__() )
print( foo.__next__() )
try:
    print( foo.__next__() )
except: print( "Nu a mers." )

for n in generatorTest():
    print(n)
 
print("######################################################################")

def genFib():
    fib1 = 0
    fib2 = 1
    while True:
        next = fib1 + fib2
        yield next
        fib1 = fib2
        fib2 = next
        

fib = genFib()
print(fib)

print( fib.__next__() )