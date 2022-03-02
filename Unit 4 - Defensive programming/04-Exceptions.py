# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:45:30 2022

@author: Silviu
"""


# RaisingExceptions
# =============================================================================
# def fancy_divide(list_of_numbers, index):
#     try:
#         try:
#             raise Exception("0")
#         finally:
#             denom = list_of_numbers[index]
#             for i in range(len(list_of_numbers)):
#                 list_of_numbers[i] /= denom
#     except Exception as ex:
#         print(ex)
# =============================================================================


# =============================================================================
# def fancy_divide(list_of_numbers, index):
#     try:
#         try:
#             denom = list_of_numbers[index]
#             for i in range(len(list_of_numbers)):
#                 list_of_numbers[i] /= denom
#         finally:
#             raise Exception("0")
#     except Exception as ex:
#         print(ex)
# =============================================================================


def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]

def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        print('Dude!!!')
        return 0