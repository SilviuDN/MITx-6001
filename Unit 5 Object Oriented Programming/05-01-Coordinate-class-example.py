# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 15:29:47 2022

@author: Silviu
"""


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance( self, other ):
        x_diff_sq = ( self.x - other.x ) ** 2
        y_diff_sq = ( self.y - other.y) ** 2
        return ( x_diff_sq + y_diff_sq )**0.5
    def __str__(self):
        return "<" + str( self.x ) + "," + str( self.y ) + ">"
    def __sub__(self, other ):
        return Coordinate( self.x - other.x , self.y - other.y )
    def __add__(self, other ):
        return Coordinate( self.x + other.x , self.y + other.y )
    def __eq__(self, other ):
        return ( self.x ==  other.x ) and ( self.y == other.y )
    
c = Coordinate( 3, 4 )
origin = Coordinate( 0, 0 )
d = Coordinate( 1, 1 )

print('Distanta dintre cele doua puncte este: ', c.distance( origin ))
print('Distanta dintre cele doua puncte este: ', Coordinate.distance( c, origin ))

#print( c.__str__)
print( c )
#print( c.__sub__.__str__ )
print( c - d )
print( c + d )
print( c == d )
print( c == c )