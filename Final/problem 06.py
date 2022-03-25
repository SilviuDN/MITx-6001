# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 20:48:07 2022

@author: SIlviu
Problem 6
"""

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: It is obvious that ' + Person.say(self,stuff)
    def lecture(self, stuff):         
        return 'It is obvious that ' + Person.say(self,stuff)

    
p1 = Person('eric')
print(p1)
print(p1.say('lol'))

l1 = Lecturer('eric')
print(l1)
print(l1.say('lol'))
print(l1.lecture('lol'))

p1 = Professor('eric')
print(p1)
print(p1.say('lol'))

ap1 = ArrogantProfessor('eric')
print(ap1)
print(ap1.say('the sky is blue'))
print(ap1.lecture('the sky is blue'))