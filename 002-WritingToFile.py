# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 21:26:49 2022

@author: Silviu
"""

import os

nameHandler = open('test10', 'w')

for i in range(3):
    name = input('Enter name: ')
    if name == 'stop': continue
    nameHandler.write(name + '\n')
    
nameHandler.close()

nameFile = open('test10', 'r')

for line in nameFile:
    print(line)
    
nameFile.close()
                   
deleteFile = input( "Delete file? ( y/n )")  
if deleteFile == 'y':
    os.remove('./test10')