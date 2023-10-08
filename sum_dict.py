# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 12:43:49 2023

@author: hp
"""

dict1 = { 'f' : 0 , 'i':1 , 'b': 1 , 'o':2 , 'n':3 , 'a': 5 , 'C':8 ,'c':13 , 'I':21} 
print("Printing dictionary...\n" , dict1)
def sumOfDict(dict):
    sumD = 0
    for i in dict1:
        sumD = sumD + dict1[i]
    return sumD 
result = sumOfDict(dict1)
print("Sum of all items -> " ,result)