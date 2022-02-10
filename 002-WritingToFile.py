# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 21:26:49 2022

@author: Silviu
"""

nameHandler = open('.gitignore', 'w')

for i in range(3):
    name = input('Enter name: ')
    if name == 'stop': continue
    nameHandler.write(name + '\n')
    
nameHandler.close()

nameFile = open('.gitignore', 'r')

for line in nameFile:
    print(line)
    
nameFile.close()
                     