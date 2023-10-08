# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 18:20:16 2023

@author: hp
"""

from functools import reduce
list1 = [1, 2, 3]
print("The list is " , list1)
 
result1 = reduce((lambda x, y: x * y), list1)
print("product of elements in list is " ,result1)