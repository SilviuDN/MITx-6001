# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:35:36 2022

@author: Silviu
"""

num = 2
word = 'two'

(num, word) = (word, num)

print('numarul e ', num)
print('Se citeste ', word)


inputData = ( (1, 'a'), (2, 'b'), (3,'c'), (4,'d') )

def separateData( aTuple ):
    numbers = ()
    letters = ()
    for tup in aTuple:
        numbers += ( tup[0],)
        letters += ( tup[1],)
    return (numbers, letters )

res = separateData(inputData)

print(res[0], res[1])