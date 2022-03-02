# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:20:48 2022

@author: Silviu
"""
a='y'
while a != 'x':
    try:
        a = input( "The divident is: ") 
        print(a)
        #a = int( input( "The divident is: ") )
        b = int( input ( "The divisor is: ") )
        print(b)
        print("a/b = ", a/b)
    except ValueError:
        print('The inserted value cannot be converted.')
    except TypeError:
        print('Only numbers should be provided.')
    except ZeroDivisionError:
        print('Divisor should not be null.')
    except:
        print('Something wrong happened.')
    else:
        print("Nice job!")
    finally:
        "Thanks for playing!"
    a = input("One more try? Enter x to Exit. ")
        